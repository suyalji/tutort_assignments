"""
Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.
You may assume that each input would have exactly one solution, and you may not use the same element twice.
You can return the answer in any order.
Example 1:
Input: nums = [2,7,11,15], target = 9
Output: [0,1]
Output: Because nums[0] + nums[1] == 9, we return [0, 1].
Example 2:
Input: nums = [3,2,4], target = 6
Output: [1,2]
Example 3:
Input: nums = [3,3], target = 6
Output: [0,1]
Constraints:
2 <= nums.length <= 104
-109 <= nums[i] <= 109
-109 <= target <= 109
Only one valid answer exists.
Follow-up: Can you come up with an algorithm that is less than O(n2) time complexity?
"""
def solution_1(arr,target): # Order of n2
    n = len(arr)
    for i in range(n): 
        for j in range(i+1,n):
            if arr[i] + arr[j] == target:
                return [i,j]
    return None    

def solution_2(arr,target):
    my_dict = {}
    n = len(arr)
    for i in range(n):
        b = target - arr[i]
        if b in my_dict.keys():
            return [i,my_dict[b]]
        else:
            my_dict[arr[i]] = i     

def solution_3(nums,target):
    buffer_dictionary = {}
    for i in range(len(nums)):
        if nums[i] in buffer_dictionary:
            return [buffer_dictionary[nums[i]], i]
        else:
            buffer_dictionary[target - nums[i]] = i    

# Driver
if __name__ == "__main__":
    inputs = [[2,7,11,15],[3,2,4],[3,3],[2,7,11,15]]
    target = [9,6,6,9]
    count = 0
    for arr in inputs:
        count += 1
        print(f"Case : {count}")
        print(f"Solution_1 : {solution_1(arr,target[count-1])}")
        print(f"solution_2 : {solution_2(arr,target[count-1])}")
        print(f"solution_3 : {solution_3(arr,target[count-1])}")