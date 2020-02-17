import random
import pytest

from sortings import merge_sort, quick_sort

@pytest.fixture()
def random_array(k=100):
    return random.sample(range(10000), k)

def test_merge_sort(random_array):
    n = len(random_array)
    assert(sorted(random_array) == merge_sort(random_array, n))

def test_quick_sort(random_array):
    n = len(random_array)
    assert(sorted(random_array) == quick_sort(random_array, n))