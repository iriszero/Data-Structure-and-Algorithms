import random
import pytest

from sortings import merge_sort, quick_sort

@pytest.fixture()
def random_array(k=100000):
    return random.sample(range(10000000), k)

@pytest.fixture()
def sorted_array(k=100000):
    return [i for i in range(k)]

@pytest.fixture()
def duplicative_array(k
=100000):
    return [7] * k

def test_merge_sort(random_array):
    n = len(random_array)
    assert(sorted(random_array) == merge_sort(random_array, n))

def test_quick_sort_random(random_array):
    n = len(random_array)
    assert(sorted(random_array) == quick_sort(random_array, n))

def test_quick_sort_edges(sorted_array, duplicative_array):
    n = len(sorted_array)
    assert(sorted(sorted_array) == quick_sort(sorted_array, n))
    
    n = len(duplicative_array)
    assert(sorted(duplicative_array) == quick_sort(duplicative_array, n))