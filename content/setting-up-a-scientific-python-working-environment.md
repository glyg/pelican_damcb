title: Setting up my python working environment
tags:scipy, howto
date: 2013-10-29 12:38:15
slug: setting-up-a-scientific-python-working-environment


Hey there... Here is the procedure I used to have a nice scientific
python stack, fitting my needs anyways, starting with a fresh linux
Mint 15 install.

<!-- TEASER_END -->

## The basics

### ssh and git

	sudo apt-get install openssh-client openssh-server
	sudo apt-get install git git-el git-gui gitk

### Those are always useful

I fail to understand why this is not in all decent distribution:

	sudo apt-get install imagemagick inkscape

Although I use less and less latex, here it is anyway

	sudo apt-get install texlive-common texlive-lang-french texlive-lang-english\
		texlive-lang-spanish texlive-doc-en texlive-fonts-extra texlive-xetex texlive-extra-utils

### emacs (yeah sublime text *is* nifty, but it's not free)

	sudo apt-get install emacs emacs-goodies.el emacsen-common
	sudo apt-get install pylint pyflakes python-nose # code checkers

`jed` is a light text-mode only emacs

	sudo apt-get install jed

The `emacs for python` repo provides all you need to have nice python features
in emacs, such as syntax checks, completion etc.

	cd .emacs.d
	git clone git://github.com/gabrielelanaro/emacs-for-python.git

Also add this to `.emacs`:

``` lisp
(load-file "/home/guillaume/.emacs.d/emacs-for-python/epy-init.el")
(epy-setup-checker "pyflakes %f")
(epy-setup-ipython)
(require 'highlight-indentation)
(add-hook 'python-mode-hook 'highlight-indentation)

(defun tv-insert-python-header ()
  "insert python header at point"
  (interactive)
  (insert "# -*- coding: utf-8 -*-\n\n"
	  "from __future__ import unicode_literals\n"
	  "from __future__ import division\n"
	  "from __future__ import absolute_import\n"
	  "from __future__ import print_function\n"))

(global-set-key (kbd "C-c e p") 'tv-insert-python-header)
```

### python setuptools and compilers

``` bash
sudo apt-get install python-setuptools build-essential python-pip\
	python-virtualenv python3-setuptools python3-pip\
	gfortran gfortran-multilib
```

## Using Python 3

### Creating a Python 3 virtual environment

pyvenv is now distributed with the library

``` bash
cd ~
pyvenv3-3 --system-site-packages python3
source python3/bin/activate
```
We also need to install distribute and pip in the virtual environment

``` bash
wget http://python-distribute.org/distribute_setup.py python3
distribute_setup.py easy_install3 pip
```

### Scientific python (3) here I come

``` bash
sudo apt-get install libfreetype6-dev libpng12-dev
sudo apt-get install python3-pyqt4 python3-pyside python3-sip\
	python3-gi python3-gi-cairo python3-cairo\ # Those are for GTK+ (not so obvious, is it?)

sudo apt-get install liblapack3 liblapack3-dev libblas3 libblas3-dev\
	libatlas3-base liblapack3gf libblas3gf libatlas3gf-base \
	libatlas-base-dev libatlas-dev liblapack3-dev  libhdf5-7 libhdf5-dev
```


There are three recommanded ways to install python packages, from the
easyest to the "edgiest".

 * Using the distribution provided packages (which will be seen in the
   virtualenv thanks to the `--system-site-packages` flag above)
 * Using pip install (which will install them in the virtual environment)
 * Getting the latest versions from github

``` bash
pip-3.3 install numpy
pip-3.3 install scipy
pip-3.3 install numexpr cython tables
pip-3.3 install matplotlib
pip-3.3 install pyzmq jinja2
pip-3.3 install ipython
pip-3.3 install pandas
pip-3.3 install scikit-image scikit-learn
```

We use Christoph Gohlke's fabulous `tifffile.py` to parse tifffiles.

``` bash
wget http://www.lfd.uci.edu/~gohlke/code/tifffile.py
tifffile.py ~/python3/lib/python3.3/site-packages/
```


## Using Python 2

### Creating a Python 2 virtual environment


``` bash
sudo apt-get install python-virtualenv
virtualenv --system-site-packages python2
source python3/bin/activate
```
Distutils and pip are installed automatically


### Scientific python (2) here I come

Here, as I want to go a bit faster, and as admitedly this version of
python willl be supported by less cutting edge packages, I install base packages
through apt (ok except IPython because it's really moving rapidly right now):

``` bash
sudo apt-get install python-gtk2 python-pyside python-pyqt
sudo apt-get install python-numpy python-scipy python-matplotlib

pip install pyzmq jinja2 tornado ipython
pip install numexpr cython tables
pip install pandas
pip install scikit-image scikit-learn
wget http://www.lfd.uci.edu/~gohlke/code/tifffile.py
mv tifffile.py ~/python2/lib/python2.7/
```

## [Graph tool](http://graph-tool.skewed.de)


What is graph-tool?

From graph-tool website:

> Graph-tool is an efficient Python module for manipulation and  statistical analysis of graphs (a.k.a. networks). Contrary to most other python modules with similar functionality, the core data structures and algorithms are implemented in C++, making extensive use of template metaprogramming, based heavily on the Boost Graph Library. This confers it a level of performance which is comparable (both in memory usage and computation time) to that of a pure C/C++ library.

Add this to `/etc/apt/sources.list`:

	deb http://downloads.skewed.de/apt/raring raring universe
	deb-src http://downloads.skewed.de/apt/raring raring universe

Replace `raring` above with your distribution (or the parent Ubuntu/Debian distro).
Then download the public key from the website and add it with apt-key
as instructed in graph-tool's website.

``` bash
apt-key add <key filename>
sudo apt-get update
sudo apt-get install python3-graph-tool python-graph-tool
```

That should be it...
