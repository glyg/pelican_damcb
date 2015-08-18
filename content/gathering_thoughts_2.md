title: From leg-joint to tyssue, a refactoring story - Ep. 2
slug: gathering_thoughts
date:
tags: drosophila, modeling, python, scipy
summary: I'm giving a talk at Euroscipy '15 in two weeks \o/ \o/... This post is a place to gather thoughts on the `leg-joint` and `tyssue` libraries, of which I'll be talking - episode 2 of 3.

That's the second blog post of three reflecting on the modeling.

1. [Performance](gathering_thoughts.html) - read this first !
2. Future plans - the future is already here
3. Visualization - even more future !


## Previously

I started optimizing, then refactoring the `leg-joint` code to gain performance.
As I was doing this, I realized it would be cleverer to go all the way back to
the drawing board (actually a paper notebook), as maybe some parts of the
simulation could be re-used with different geometries. After all, many epithelia
share common traits with the leg imaginal disk. At the same time, Magali and I
started talking with two physicists, [François
Molino](http://www.coulomb.univ-montp2.fr/user/francois.molino) and  [Cyprien
Gay](http://www.msc.univ-paris-diderot.fr/~cgay/homepage/doku.php?id=Accueil),
who are applying bleeding edge soft-matter physics to biological tissues. It
turns out Cyprien and his colleges recently published a [milestone
paper](http://dx.doi.org/10.1140/epje/i2015-15033-4) on continuous models; both
were keen on trying cell based models, and the leg disk is of course very rich
on this regard. So while I'm generalizing geometry, why not physics?

So how do we get there?

1. Classify existing biophysical tissue models.

2. Specify the subset of said models we want to address.

3. Try to craft an API.

4. Choose the proper libraries.

5. Code simple test cases (simple geometry, simple physics).

6. Repeat from 3 until the API and tech are +/- stable...

7. Implement a real world problem, same physics as in 5.

8. Try new physics at constant geometry.



### A very brief tour of the biophysical models of living tissues

As they imply dramatic changes in a tissue shape and organization, morphogenetic
events have long been the focus of mechanical modeling efforts. As early as
1917, D'Arcy Thomson exposed the underlying mathematical and physical
relationships underpinning cells and multi-cellular organism shapes and
dynamical behaviors (in the seminal work [On Growth and
Form](https://archive.org/details/ongrowthform00thom)). In recent years,
technical progresses have provided very detailed geometrical, dynamical and
biochemical data on morphogenetic processes, allowing for ever finer
mathematical modeling and computer simulations. Meanwhile, many models and
simulations have been developed. The interested reader will find a very clear,
useful and complete discussion of the topic in [C.V.T Tamulonis PhD
dissertation](http://dare.uva.nl/record/1/394902). Seriously, I can't stress
enough how this work is nice and complete!


For now, I just drafted a tree of the different models, as a basis for the
discussion:

![Tissue models family tree](images/models_family_tree.png)

The underlying dragonfly wing is from figure 162 of _On Growth and Form_ (p.476
of the above linked edition). On the last line are examples (not even close to
exhaustive) of implementation for each models. 

Continuous models deal with phenomena that span multiple cells in size, such
that the changes in shape can be smoothed out, the detailed cell-cell
interactions are not necessary to understand the tissue's shape. They are out of
focus for now, so let's concentrate on _cell based models_.
