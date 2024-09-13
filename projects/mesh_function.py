import numpy as np


def mesh_function(f, t):
    return f

def func(t):
    return np.exp(-t)

def test_mesh_function():
    t = np.array([1, 2, 3, 4])
    f = np.array([np.exp(-1), np.exp(-2), np.exp(-3), np.exp(-4)])
    fun = mesh_function(func, t)
    assert np.allclose(fun, f)
