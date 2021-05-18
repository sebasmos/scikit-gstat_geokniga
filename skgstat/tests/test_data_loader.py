from skgstat import data
import numpy as np
from numpy.testing import assert_array_almost_equal


def test_data_names():
    assert 'pancake' in data.names


def test_loader():
    img = data.pancake_field()

    assert img.shape[0] == 500 and img.shape[1] == 500


def test_sample():
    c, v = data.pancake(N=50)

    assert len(c) == len(v) == 50


def test_loader_mean():
    c0, v0 = data.pancake(N=10, band=0)
    c1, v1 = data.pancake(N=10, band=1)
    c2, v2 = data.pancake(N=10, band=2)
    cm, cv = data.pancake(N=10, band='mean')

    # manually calculate the mean
    mean = np.mean(np.column_stack((v0, v1, v2)), axis=1)
    print(mean)

    assert_array_almost_equal(cv, mean, decimal=4)
