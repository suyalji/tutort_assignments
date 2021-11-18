""" 
Given an array nums of size n, return the majority element.
The majority element is the element that appears more than ⌊n / 2⌋ times. You may assume that the majority element always exists in the array.
Example 1:
Input: nums = [3,2,3]
Output: 3
Example 2:
Input: nums = [2,2,1,1,1,2,2]
Output: 2
Constraints:
n == nums.length
1 <= n <= 5 * 104
-231 <= nums[i] <= 231 - 1
Follow-up: Could you solve the problem in linear time and in O(1) space?
"""
def solution(nums):
    n = len(nums)
    my_dict = {}
    for i in nums:
        if i in my_dict.keys():
            my_dict[i] = my_dict[i] +1
        else:
            my_dict[i] = 1    
    for key,value in my_dict.items():
        if value > int(n/2):
            return key
    return None        

if __name__ == "__main__":
    inputs = [[3,2,3],[2,2,1,1,1,2,2]]
    for arr in inputs:
        print(f"Input : {arr}")
        print(f"Solution : {solution(arr)}")
