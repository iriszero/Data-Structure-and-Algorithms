import unittest
import random

def merge_sort(arr, n):
    '''
    W(n) = 2W(n/2) + O(n) = O(nlogn)
    S(n) = O(n)

    extra space - O(n)
    not in-place
    '''
   
    # base case
    if n==1:
        return arr
    
    # n>=2 
    left_len = n // 2 # (>=1)
    right_len = n - n//2 # (>=1)

    left_arr = merge_sort(arr[:left_len],left_len)
    right_arr = merge_sort(arr[left_len:],right_len)
    
    new_arr = []
    left_idx = 0
    right_idx = 0

    while left_idx < left_len and right_idx < right_len:
        left_elem = left_arr[left_idx]
        right_elem = right_arr[right_idx]

        if left_elem < right_elem:
            new_arr.append(left_elem)
            left_idx += 1
        else:
            new_arr.append(right_elem)
            right_idx += 1
    
    while left_idx < left_len:
        left_elem = left_arr[left_idx]
        new_arr.append(left_elem)
        left_idx += 1
    
    while right_idx < right_len:
        right_elem = right_arr[right_idx]
        new_arr.append(right_elem)
        right_idx += 1
    
    return new_arr

def quick_sort(arr, n):
    def _partition(arr, left, right):
        """
        the indices are inclusive
        """

        i = left
        pivot = arr[right]

        # keep arr[i..j-1] are all smaller than the pivot and
        # arr[j+1..] are all larger than the pivot

        for j in range(left, right):
            if arr[j] < pivot:
                arr[i], arr[j] = arr[j], arr[i]
                i += 1
        
        arr[i], arr[right] = arr[right], arr[i]
        return i
    
    def _select_pivot(arr, left, right):
        def _pick_pivot(arr, left, right):
            # the right most
            # return right

            # random
            return random.randint(left, right)

        pi = _pick_pivot(arr, left, right)
        arr[pi], arr[right] = arr[right], arr[pi]
        return arr[right]

    def _three_way_partition(arr, left, right):
        """
        [left, i) <pivot
        [i, j) =pivot
        [j, k) not examined
        [k, right) >pivot
        """

        pivot = _select_pivot(arr, left, right)
        i = left
        j = left
        k = right 

        while j <= k:
            if arr[j] < pivot:
                arr[i], arr[j] = arr[j], arr[i]
                i += 1
                j += 1
            elif arr[j] > pivot:
                arr[j], arr[k] = arr[k], arr[j]
                k -= 1
            else:
                j+= 1

        return i, k
    
    def _quick_sort(arr, left, right):
        if left>=right:
            return

        l, r = _three_way_partition(arr, left, right)
        _quick_sort(arr, left, l-1)
        _quick_sort(arr, r, right)

    _quick_sort(arr, 0, n-1)
    return arr

def insertion_sort(arr, n):
    pass

def selection_sort(arr, n):
    pass

def bubble_sort(arr, n):
    pass

sort_functions = [merge_sort, quick_sort, insertion_sort, selection_sort, bubble_sort]