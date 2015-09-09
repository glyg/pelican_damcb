title: The leg joint paper is out!
slug: paper_out
date: 02-12-2015
tags: drosophila, modeling
summary: Our work on the role of apoptosis in morphogenesis is out today!


We did it! After nearly three years of work (the initial commit to the
[code](https://github.com/glyg/leg-joint) was done on may 24th 2014),
the work on the role of apoptosis in the formation of folds in
epithelium is [out](http://dx.doi.org/10.1038/nature14152)!

I'm very proud for this work. Of course most of the credit goes to
[Magali Suzanne team](http://www-lbcmcp.ups-tlse.fr/Nouveau_site/modeles/EquipeSuzanne-Accueil.htm).
This is top quality biology, and it was really nice being part of the
research process.  The model itself relies on the marvelous scientific
python ecosystem and its supporting community. Special thanks to Tiago
for providing the [graph-tool](http://graph-tool.skewed.de/) library.

The code is described in details in a series of Ipython Notebook that
you can read
[here](http://nbviewer.ipython.org/github/glyg/leg-joint/tree/master/notebooks/).

Now for a brief summary on what we did:

**[edit 01/23]** there's a nice news and views
  [here](http://dx.doi.org/10.1038/nature14198) where
  [Claudia Vasquez and Adam Martin](http://web.mit.edu/martin-lab/research.html) review the biology and rise interesting questions.

### Apoptotic cells last stand - and its consequences for morphogenesis

_We showed that, far from being passively eliminated, apoptotic cells
do actively influence their environment by increasing the surrounding
tissue tension. Indeed, before they die, apopotic cells exert a force
that transiently deform the apical surface of the epithelium. This
force is then transmitted to the neighbouring cells through an increase
in tension which will in turn provoke a change in tissue shape._

Apoptosis is known for its role in morphogenesis, and more specifically
in the formation of folds in various developmental contexts; yet the
molecular mechanisms implied in those processes remain largely
unknown. The formation of folds within an epithelium allows to pass
from a bidimentional to a tridimentional tissue and is thus a key step
in morphogenesis. Here we showed a new mechanism of fold formation in
the
[Drosophila leg disk](https://en.wikipedia.org/wiki/Imaginal_disc). This
mechanism not only implies the elimination of apoptotic cells from the
tissue, but also their active participation to the tissue
remodelling. Indeed, each apoptotic cells within the epithelium
generates before it dies a force relying on the establishment of an
apico-basal acto-myosin cable. This previously unknown cable drives a
transitory deformation of the apical surface of the epithelium, which
in turn drives a stabilization of myosin II in the neighbouring cells
at the adherent junctions level, as well as an increase in tissue
tension. We also showed that the synergistic contribution of several
apoptotic cells was necessary to create a myosin II stabilization in
the whole neighbouring tissue, a global increase in tension, cells
apical constriction and eventually the fold formation.

Finally, in order to test whether those apoptotic forces are indeed the
initial signal responsible for the change in tissue shape, we devised
a 3D model of the leg disk epithelium, based on the pre-existing
vertex model published by
[Farhadifar et al.](10.1016/j.cub.2007.11.049) in 2007. In this
bio-mechanical model, we were able to show that apoptotic forces (the
apical-basal force, followed by the apical propagation) are both
necessary and sufficient to drive fold formation, suggesting that this
new mechanism could happen in any type of epithelium.

This work is an important step in the field of morphogenesis and
brings up a new dogma on the active role of apoptosis in apoptotic cells.

Bellow is a movie of the formation of the leg joint _in vivo_ (that's
confocal microscopy, apoptotic cells are marked red:

<iframe src="//player.vimeo.com/video/109897311" width="500"
height="428" frameborder="0" webkitallowfullscreen mozallowfullscreen
allowfullscreen></iframe> <p><a
href="http://vimeo.com/109897311">Apical vue of the fold formation on
a drosophila leg disk</a> from <a
href="http://vimeo.com/user12210065">glyg</a> on <a
href="https://vimeo.com">Vimeo</a>.</p>

And a movie of the simulated tissue undergoing fold formation:

<iframe src="//player.vimeo.com/video/107188046" width="500"
height="500" frameborder="0" webkitallowfullscreen mozallowfullscreen
allowfullscreen></iframe> <p><a href="http://vimeo.com/107188046">Fold
formation model</a> from <a
href="http://vimeo.com/user12210065">glyg</a> on <a
href="https://vimeo.com">Vimeo</a>.</p>

Of course my work with Magali's team continues, and there's a lot more
to investigate: the precise mechanism by which the apical-basal force
is translated in an apical myosin accumulation, the role of cell
polarity in the process, or the role of the peripodial membrane in shaping the tissue, for example. Exciting times!
