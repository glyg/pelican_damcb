title: Setting up my python working environment
tags: scipy, howto
date: 05-15-2014
slug: setting-up-a-scientific-python-working-environment


**Updated !!** Hey there... Here is the procedure I used to have a
nice scientific python stack, fitting my needs anyways, starting with
a fresh linux Mint 17 install. Please note that things got a _lot_
simpler with the latest
[anaconda](https://store.continuum.io/cshop/anaconda/) releases.

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

Also add this to `.emacs` (changing `USERNAME` to your user name...):

``` lisp
(load-file "/home/USERNAME/.emacs.d/emacs-for-python/epy-init.el")
(epy-setup-checker "pyflakes %f")
(epy-setup-ipython)
(require 'highlight-indentation)
(add-hook 'python-mode-hook 'highlight-indentation)

;;; Bellow is a header with what's need for python 2.7 compatibility
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

### Compilers

``` bash
sudo apt-get install build-essential gfortran gfortran-multilib
```


## Using Python 3

Since I first wrote this post, I started using [anaconda](https://store.continuum.io/cshop/anaconda/) for my basic installation. It really eases the management and creation of virtual environments, updates and package management. In a recent update, you can have a 'native' python 3.4 install.


After downloading anaconda from the above link (they ask for your
email but that doesn't translate into flows of spam), just run the
installer :

```bash
cd directory/where/youdownloaded/thefile
### you might need to chmod the script
chmod +x Anaconda-2.0.1-Linux-x86_64.sh
./Anaconda-2.0.1-Linux-x86_64.sh
### update your bashrc to take into account the new paths
source ~/.bashrc
```


### Creating a Python 3 virtual environment

Easy as pie:
```bash
conda create -n python3 python=3 anaconda
```
Now you can use this new environment by tiping:

```bash
source activate python3
```

Your terminal prompt should now be prepended with a `(python3)` string

Note that `python3` here is just a name, you can use anything you want. Also some advocate the use of one virtual environment for each project... I'm not very fond of this strategy.

If you need recent packages, that might not be included in the conda distribution, you can use `pip` from whithin the virtual environment, as so:

```
pip install --upgrade scikit-image
```

We use Christoph Gohlke's fabulous `tifffile.py` to parse tifffiles.

``` bash
wget http://www.lfd.uci.edu/~gohlke/code/tifffile.py
mv tifffile.py ~/python3/lib/python3.3/site-packages/
```

The whole procedure is way easier than it use to be in the old days. Most of the time they ship the latest stable of the packages. Furthermore, it is common practice in the exosystem to test ones package through travis continuous integration by installing MiniConda and the required packages... So you end up with a vetted set of libraries.



## Using Python 2

### Creating a Python 2 virtual environment

You guessed it:

```bash
conda create -n python2 python=2.7 anaconda
```

I think if you just say `python=2` it will install version 2.6, which you only want if you have to develop with it for legacy reasons (but even debian stable ships 2.7, so that should be a rare occurence by now).


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

### link the packages to the respective environments

As `graph-tool` is not included (yet?) in conda, and the compilation is, well, complicated, we have to link the library to our packages:

```bash
ln -s /usr/lib/python3/dist-packages/graph_tool /home/USER/anaconda/envs/python3/lib/python3.4/site-packages/graph_tool
ln -s /usr/lib/python2.7/dist-packages/graph_tool /home/USER/anaconda/envs/python2/lib/python2.7/site-packages/graph_tool
```

### Some more stuffs

I added this in my `.bashrc` for git clarity (thanks to Hadrien Mary
aka @hadim):

```bash
## git status in prompt
export PS1='\[\033[01;32m\]\h\[\033[01;34m\] \w\[\033[01;33m\]$(__git_ps1)\[\033[01;34m\] \$\[\033[00m\] '
# export PS1='\[\033[01;32m\]\u@\h\[\033[01;34m\] \w\[\033[01;33m\]$(__git_ps1)\[\033[01;34m\] \$\[\033[00m\] '
export GIT_PS1_SHOWDIRTYSTATE=1
```
