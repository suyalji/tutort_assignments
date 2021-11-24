""" 
Given an array nums, return true if the array was originally sorted in non-decreasing order,
then rotated some number of positions (including zero). Otherwise, return false.
There may be duplicates in the original array.
Note: An array A rotated by x positions results in an array B of the same length 
such that A[i] == B[(i+x) % A.length], where % is the modulo operation.
"""
import sys
def solution(nums):
    n = len(nums)
    prev = nums[0]
    count = 0
    junction = -(sys.maxsize)
    for i in range(1,n):
        if nums[i] > prev and nums[i] < junction:
            print("ok")
        elif nums[i] < prev:
            count += 1 
            junction = prev
        if count == 0 or count == 1:
            return True
        else :
            return False    
if __name__ == "__main__":
    inputs = [[6,1,2,3,4,5],[1,2,3,4,5],[2,1,3,4]]
    for arr in inputs:
        print(solution(arr))
        print("--------------------------------------------------------------")