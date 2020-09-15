import numpy as np
arr = [87, 66, 13, 120, 14, 19]
def binary_search(arr, el, start, end):
    mid = (start + end) // 2
    if el == arr[mid]: 
        return mid
    if el < arr[mid]:
        return binary_search(arr, el, start, mid-1)
    else:
        return binary_search(arr, el, mid+1, end)
print(binary_search(arr, 120, 0, len(arr)))

def sorting(arr):
    arr.sort()
    return arr
print(sorting(arr))

def merge():
    a = [11, 56, 28, 45, 86, 2]
    b = [9, 77, 40]
    merged_list = np.concatenate((a,b))
    return merged_list    
print(merge())

def rev():
    rev_list = np.flipud(arr)
    return rev_list
print(rev())
