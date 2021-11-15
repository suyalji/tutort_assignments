""" 
1. Find the position of first occurance
2. Find the position of last occurance

"""
arr = [1,2,3,4,4,4,5,6,7]

def sulution(arr):
    target = 4 
    n = len(arr)
    low = 0
    hign = n-1

    if arr[low] == target:
        return low
    mid = (low+high)/2
    if target == mid:
        index = mid
        high = mid-1
    elif target > mid:
        low = mid
    elif target < mid:
        high = mid
    











