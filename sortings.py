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
    pass

def insertion_sort(arr, n):
    pass

def selection_sort(arr, n):
    pass

def bubble_sort(arr, n):
    pass

sort_functions = [merge_sort, quick_sort, insertion_sort, selection_sort, bubble_sort]