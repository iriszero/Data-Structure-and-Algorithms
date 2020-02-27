import random
import pytest

from sortings import merge_sort, quick_sort
from test_constatns import *

ELEM_MAX  = 10000000
SZ_ARR = SZ_LARGE
TIMEOUT = SZ_LARGE

@pytest.fixture()
def random_arr(k=SZ_ARR):
    return random.sample(range(ELEM_MAX), k)

@pytest.fixture()
def sorted_arr(k=SZ_ARR):
    return [i for i in range(k)]

@pytest.fixture()
def dup_arr(k=SZ_ARR):
    return [7] * k

def test_merge_sort(random_arr):
    n = len(random_arr)
    assert(sorted(random_arr) == merge_sort(random_arr, n))

def test_quick_sort_random(random_arr):
    n = len(random_arr)
    assert(sorted(random_arr) == quick_sort(random_arr, n))

@pytest.mark.timeout(TIMEOUT)
def test_quick_sort_edge1(sorted_arr):
    n = len(sorted_arr)
    assert(sorted(sorted_arr) == quick_sort(sorted_arr, n))

@pytest.mark.timeout(TIMEOUT)
def test_quick_sort_edge2(dup_arr):
    n = len(dup_arr)
    assert(sorted(dup_arr) == quick_sort(dup_arr, n))