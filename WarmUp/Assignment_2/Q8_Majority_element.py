"""
Given an integer array nums sorted in non-decreasing order and an integer target, return true if target is a majority element, or false otherwise.
A majority element in an array nums is an element that appears more than nums.length / 2 times in the array.
Example 1:
Input: nums = [2,4,5,5,5,5,5,6,6], target = 5
Output: true
Explanation: The value 5 appears 5 times and the length of the array is 9.
Thus, 5 is a majority element because 5 > 9/2 is true.
"""
def solution_1(arr):
    my_dict = {}
    n = len(arr)
    for i in arr:
        if i in my_dict.keys():
            my_dict[i] = my_dict[i]+1
        else:
            my_dict[i] = 1    
    for key,value in my_dict.items():
        if value > n/2:
            return True
    return False        


if __name__ == "__main__":
    inputs = [[2,4,5,5,5,5,5,6,6],[10,100,101,101],[0] ]
    for arr in inputs:
        result = solution_1(arr)
        print("Solution_1",result)


