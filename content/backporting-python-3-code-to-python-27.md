title: Backporting python 3 code to python 2.7
slug: backporting-python-3-code-to-python-27
date: 04-23-2014
tags: python, 3to2
summary:An adventure in backporting, unfiltered for stupid mistakes

We decided to develop
[scikit_tracker](https://github.com/bnoi/scikit-tracker) in python 3.x,
and test only against this brand of python, because all the Scipy
stack is ported now, so why not.

Unfortunately, our first user (whom we don't want to scare off) uses
[canopy](https://www.enthought.com/products/canopy/), which is python 2.7.

So I thought I would document the porting of the code, so here we go.

<!-- TEASER_END -->

## A script to put a correct header on top of each file.

Adding `__from__ future import ...` statements on top of your file goes
a long way in porting the code, making most of the new feature from
python 3 available to 2.x code.

I'm sure there's a `sed` one liner to do that, but I'm just more efficient with python:

### Recursively find all the python file in the project's directory

```python
pyfiles = []
for root, subFolders, files in os.walk(base_dir):
    for f in files:
        if f.endswith('.py'):
            pyfiles.append(os.path.join(base_dir, root, f))
```

### Check we really got files:

```python
import numpy as np
print('''All files ok: {}'''.format(np.all([os.path.isfile(fname)
                                    for fname in pyfiles])))
```

Adding imports and coding on top of the python files.
**TODO**: avoid adding this if it's allready there...

```python
compat_string = '''# -*- coding: utf-8 -*-

from __future__ import unicode_literals
from __future__ import division
from __future__ import absolute_import
from __future__ import print_function

'''

for fname in pyfiles:
    with open(fname, 'r+') as pyfile:
        new_f = ''.join([compat_string]+
                          [line for line in pyfile.readlines()])
    with open(fname, 'w+') as pyfile:
        pyfile.write(new_f)
```

We use `UserDict`to subclass dictionnaries, we need to modify import so I replaced this:

```python
from collections import UserDict
```

by that:

```python
if sys.version_info > (3, 0):
    from collections import UserDict
else:
    from UserDict import UserDict
```

## Using 3to2

We don't really want to do all the fixes provided by 3to2, as we only seek python 2.7 compatibility

Here is the list of possible fixes, and a comment on what it does when passed :

```bash
/home/user $ 3to2 -l
Checking Python version info... 2.7.5
Available transformations for the -f/--fix option:
annotations # says no file need modification
bitlength # says no file need modification
bytes # Only wants to modify tifffile.py and I know it works fine in both versions
classdecorator # says no file need modification
collections # messes with the correction above, which is version agnostic
dctsetcomp # that's dict comprehension, which was backported to python 2.7
division # says no file need modification
except # Only wants to modify tifffile.py and I know it works fine in both versions
features # says no file need modification
fullargspec # says no file need modification
funcattrs # says no file need modification
getcwd # says no file need modification
imports # says no file need modification
imports2 # says no file need modification
input # says no file need modification
int # Appends an L to all the ints (I guess because all ints are long ints in py3k)
intern # says no file need modification
itertools # changes zip to izip, but that's not interesting for us (py 2.7 ok I think)
kwargs  # says no file need modification
memoryview  # says no file need modification
metaclass  # says no file need modification
methodattrs  # says no file need modification
newstyle ### This one is usefull, adds (object) to the class definition
next # Only wants to modify tifffile.py and I know it works fine in both versions
numliterals  # says no file need modification
open ## Backported
print ## Fixed by from __future__
printfunction   # says no file need modification
raise   # says no file need modification
range ## Keep range for py3 compatibility
reduce # says no file need modification
setliteral # says no file need modification
str ## Fixed by from __future__
super #### Usefull
throw # says no file need modification
unittest # says no file need modification
unpacking # says no file need modification
with # New in 2.5
```

Let's resume all that:


* Usefull fixes:

```bash
newstyle, super
```

* Fixes that don't do anything:

```bash
annotations, bitlength, classdecorator, division, features,
fullargspec, funcattrs, getcwd, imports, imports2, input, intern, kwargs,
memoryview, metaclass, methodattrs, numliterals, printfunction, raise,
reduce, setliteral, throw, unittest, unpacking
```

* Fixes that would modify `tifffile.py` only (we don't want those):

```bash
bytes, except, next
```

* Fixes that are corrected by `from __future__ import ...`:

```bash
print, str
```

* Fixes that are unnecessary with python 2.7:

```bash
dctsetcomp, itertools (?), open, with
```

So now we just issue this command to port the code:

```bash
/home/user$ 3to2 -f super -f newstyle -w sktracker/ ## This is our project's directory
```

## Cleaning


Once this is done, there's quite a lot of work to fix, and have tests passing (by the way, tests are really great, seeing how many quirks I had to fix).

Now let's go through the diff to see what we had to change.

* This of course is here everywhere:

```diff
+# -*- coding: utf-8 -*-
+
+
+from __future__ import unicode_literals
+from __future__ import division
+from __future__ import absolute_import
+from __future__ import print_function
```

* Pytables HDFStore files can't be exchanged between python 2 and python 3, so we have to have two samples files for the tests

```diff

 import tempfile
 import shutil
 import pandas as pd
+import sys

 from ..io.utils import load_img_list


 def sample_h5():
     """
     """
+    if sys.version_info[0] < 3:
+        return os.path.join(data_path, "sample_py2.h5")
     return os.path.join(data_path, "sample.h5")
```

* There I guess `subprocess` is inconsistent. I think this is relatively harmless

```diff

         # module such as numpy (only needed on linux)
         if os.name == 'posix':
             subprocess.call("taskset -p 0xff %d" % os.getpid(),
-                            shell=True, stdout=subprocess.DEVNULL)
+                            shell=True)#, stdout=subprocess.DEVNULL) ## Py2.7 compat
```

* This is rather self explanatory

```diff
-from collections import UserDict
+if sys.version_info[0] > 2:
+    from collections import UserDict
+else:
+    from UserDict import UserDict
+
```

* Old style / new style classes (there are other like that)

```diff

-class ObjectsIO():
+class ObjectsIO(object):
```

* This one had to be called like that, not through `super`, maybe because `UserDict` is old style

```diff

     def __init__(self, metadata_dict, objectsio):
         self.objectsio = objectsio
-        super().__init__(metadata_dict)
+        UserDict.__init__(self, metadata_dict)
```

* Now that one involved really obscure utf-8 / unicode shenaningans, plus `io.StringIO` not working with 2.7, while creating a temp file was not with 3...

So here is what the solution looks like:

```diff
         et = ElementTree.ElementTree(self.root)

-        f = io.StringIO()
-        et.write(f, encoding='unicode', xml_declaration=True,
-                 default_namespace=None)
-        output = f.getvalue()
+        if sys.version_info[0] < 3:
+            f = tempfile.NamedTemporaryFile()
+            et.write(f, encoding='utf-8', xml_declaration=True,
+                     default_namespace=None)
+            f.seek(0)
+            output = ''.join(f.readlines())
+        else:
+            f = io.StringIO()
+            et.write(f, encoding='unicode', xml_declaration=True,
+                     default_namespace=None)
+            output = f.getvalue()
         f.close()
```

* I don't realy know why, but I had to explicitely use `BrownianLinkCostFunction` here, and not the automated  `self.__class__`

```diff
-        super().__init__(context={}, parameters=_parameters)
+        super(BrownianLinkCostFunction, self).__init__(context={}, parameters=_parameters)
```

* Unicode / string mess, I didn't really fix it up yet...

```diff
-    cost_func.check_context('test_string', str)
+    ### This fails in py2.7
+    if sys.version_info[0] > 2:
+        cost_func.check_context('test_string', str)
```

* More encoding quirks (makes you _love_ python 3):

```diff
     if message:
-        bar += " " + str(message)
+        bar = " ".join([bar, message])
```




And now all the tests are passing, which is great, have to try to get
into production now. There are still some quirks to fix (essentially anytime we call `str`).
