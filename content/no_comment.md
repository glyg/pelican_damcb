title: No comment
slug: no-comment
date: 04-04-2015
tags: pandas, optimization, scipy
summary: Speaks for itself

```python
import pandas as pd

n_times = 3
n_parts = 4


def meth1(n_times, n_parts):
    return pd.MultiIndex.from_tuples([(i,j) for (i, j) in np.ndindex((n_times, n_parts))],
                                      names=['t_stamp', 'label'])



def meth2(n_times, n_parts):
    time_stamps, labels = np.mgrid[:n_times, :n_parts]
    return pd.MultiIndex.from_arrays([time_stamps.flatten(),
                                      labels.flatten()],
                                      names=('t_stamp', 'label'))

def meth3(n_times, n_parts):
    time_stamps, labels = np.mgrid[:n_times, :n_parts]
    return pd.MultiIndex.from_arrays([time_stamps.ravel(),
                                      labels.ravel()],
                                      names=('t_stamp', 'label'))

%timeit meth1(1000, 10)
> 100 loops, best of 3: 10.5 ms per loop

%timeit meth2(1000, 10)
> 1000 loops, best of 3: 779 µs per loop

%timeit meth3(1000, 10)
> 1000 loops, best of 3: 763 µs per loop
```
