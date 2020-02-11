import random
import pytest

from sortings import merge_sort
from sortings import sort_functions

@pytest.fixture()
def random_array(k=100):
    return random.sample(range(10000), k)

def test_merge_sort(random_array):
    n = len(random_array)
    for sort_function in sort_functions:
        assert(sorted(random_array) == sort_function(random_array, n))
