""" 
Given an array nums. We define a running sum of an array as runningSum[i] = sum(nums[0]…nums[i]).
Return the running sum of nums.
"""
def runningSum(nums):
    moving = 0
    for i in range(len(nums)):
        nums[i] = nums[i] + moving
        moving = nums[i]
    return nums    

if __name__ == "__main__":
    inputs = [[1,2,3,4],[1,1,1,1,1],[3,1,2,10,1]]
    for arr in inputs:
        print(f"Solution_1 : {runningSum(arr)}")

