title: Gathering thoughts for Euroscipy 2015
slug: gathering_thoughts
date:
tags: drosophila, modelling, python
summary: I'm giving a talk at Euroscipy '15 in two weeks (waow). This post is
  a place to gather thoughts on what I'll be talking about and write
  in the proceedings.


So I'm giving a talk at Euroscipy at the end of the summer on

# The talk abstract

Biological tissues, and more particularly
[epithelia](http://en.wikipedia.org/wiki/epithelium) are very
particular kinds of material. Not only do they behave like solids
_and_ liquids at the same time (think shaving foam), they are also
governed by the behaviour of their constituent individual
cells. Biological processes (a bunch of incredibly complex chemical
reactions) and physics are intertwined so that complex forms emerge
from initially smooth tissues.

Along advanced imaging techniques and genetic manipulation of model
organism, biophysical modeling is key in understanding these shape
changes, or morphogenesis. We studied the role of programmed cell
death, or [apoptosis](http://en.wikipedia.org/wiki/apoptosis) in the
formation of a fold in the fruit fly pupae (an intermediate stage
between larva and adult). In
[a recently published article](http://dx.doi.org/10.1038/nature14152)
we demonstrated that apoptotic cells had an active role in shaping
this fold (which will later become a joint in the adult fly's
leg). Cells die on a ring around the socket shaped tissue (one cell
thick, and about 200 µm in diameter), they contract and pull on their
neighbours, initiating changes in the tissue properties.

In this presentation, I will describe how we use python to develop a
numerical model of this epithelium. The
[leg-joint](https://github.com/glyg/leg-joint) module is based on
Tiago Peixoto's [graph-tool](http://graph-tool.skewed.de) library, and
uses SciPy optimization routines to perform the gradient descent at
the core of the dynamical simulation. The following topics will be discussed:

* Visualization: plain matplotlib vs [vispy](http://vispy.org) vs
  [Blender](http://www.blender.org).

* Performance: can we go from 24 hrs per simulation to less than 1?
  The pure python vectorization and BoostPython/CGAL routes.

* Future plans: towards a biological tissue physics engine.

The code is showcased in a series of Jupyter Notebooks that can be
browsed
[here](http://nbviewer.ipython.org/github/glyg/leg-joint/tree/master/notebooks/).



# What's new since this was written

The `leg_joint` code was developed while our understanding of the biology was
progressing  at a fast pace, as Magali's team accessed new genetic tools and
gradually improved the fluorescence microscopy images of the drosophila's leg
disk. That left little room for API design, or optimization.

So I started refactoring once the paper was published. The performance
bottleneck was quite obvious: the gradient descent code was called locally (only
on a group of cells) a lot of times to mimic a global epithelium relaxation, and
this code contained explicit loops over each cell of the global patch to update
geometry and gradients **at each optimization step**. This is bad, but was easy
to write. It also made whole tissue optimization depressingly slow. As a good
SciPythonista (if that's a thing), I started looking at vectorization strategies.

I started using graph-tool for its efficient management of dynamic graphs and
graph drawing capacities. In this library, values attached to vertices and edges
can be accessed as Numpy arrays through a wrapper class called a `PropetyMap`.
You can access a subset of those values through _filtering_, i.e. defining a
binary mask over the network. But filtering is not the same as indexing, for
example you can do this with indexing:

```python
import numpy as np
a = np.arange(4) + 2
b = a[0, 1, 3, 3, 3]
print(b)
>>> [2, 3, 5, 5, 5]
```

But you can't tell a mask to repeat a value, and that was exactly what I needed
to compute my epithelium geometrical properties. With PropertyMaps, you can
*get* values from fancy indexing, but *setting* them back is more complicated,
due to the rather convoluted way graph-tool mirrors the underlying C++ data and
the property map `.a` attribute, that returns a numpy array. Of course
graph-tool was not meant for that kind of computation, it's focus is on graphs, not geometry.

The cell's area is a good example for the type of computation I was trying to
run. It is computed as the sums of the cell's sub-faces areas, which are
computed as a cross product of two sub-face vectors:

![A cell segmented in triangles](images/cell_area.png)

The area of the sub-face is $A_{\alpha ij} = || r_{\alpha i} \times r_{\alpha j} || / 2$.

Cross product works just fine with numpy arrays, but to compute it, I need to
repeat each vector twice for each adjacent face, hence my indexing issue with
graph-tool property maps. This motivated the passage to `pandas` DataFrames to
do the geometrical computing. Fancy indexing is what pandas is made for, isn't it?

Here is an outline of the strategy I used to gather the data from the graph's propertymap and turn them into dataframes:

* First find all the faces in the graph, using graph-tool's
`subgraph_isomorphism`

```python
def get_faces(graph, as_array=True):
    '''
    Retrieves all the triangular subgraphs of the form
       1 -- > 2
        ^   ^
         \ /
          0
    In our context, vertex 0 always corresponds to a cell
    and vertices 1 and 2 to junction vertices

    Parameters
    ----------
    graph : a :class:`GraphTool` graph instance
    as_array: bool, optional, default `True`
      if `True`, the output of `subraph_isomorphism` is converted
      to a (N, 3) ndarray.
    Returns
    -------
    triangles:  list of gt.PropertyMaps or (N, 3) ndarray
      each line corresponds to a triplet (cell, jv0, jv1)
      where cell, jv0 and jv1 are indices of the input graph
      if
    '''
    tri_graph = gt.Graph()
    ## the vertices
    verts = tri_graph.add_vertex(3)
    ## edges
    tri_graph.add_edge_list([(0, 1), (0, 2), (1, 2)])
    _triangles = gt.subgraph_isomorphism(tri_graph, graph)
    if not as_array:
        return tri_graph, _triangles
    triangles = np.array([tri.a for tri in _triangles], dtype=np.int)
    return triangles
```


This works thanks to the definition of the graph edges, with edges from cell
center to junction vertices always oriented outwards, such that the triangular
pattern uniquely defines the set of faces.

The `triangles` array then served as a `MultiIndex` for a pandas `DataFrame`
called `faces`. Each of the vertex index was repeated as many times as
necessary, and it was then easy to pick the correct data to compute the desired
crossproduct, and do sums for each cells (something like `faces['sub_areas'].sum(level='cell')`).

According to `git log`, it took me about three weeks to vectorize completely the geometry and gradient computation. 




I learned C++ and CGAL!
