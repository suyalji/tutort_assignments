""" 
STATUS :  NOT DONE
Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]] such that i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0.
Notice that the solution set must not contain duplicate triplets.
"""
def solution(nums):  # Brute Force O(n3)
    n = len(nums)
    out = []
    visited = []
    keep_track = {}
    for i in range(n):
        for j in range(n):
            for k in range(n):
                if (nums[i]+nums[j]+nums[k] == 0):
                    if i != j and j != k and i != k:
                        temp = sorted([nums[i],nums[j],nums[k]])
                        temp = sorted(temp)
                        key = f"{temp[0]}{temp[1]}{temp[2]}"
                        if key not in keep_track.keys():
                            keep_track[key] = 1
                            out.append(temp)
    return out

def solution_2(nums):
    n = len(nums)
    out = []
    my_dict = {}
    for i in range(n):
        for j in range(n):
            rev =  (nums[i]+nums[j])* -1
            if rev in nums:
               # print(nums[i],nums[j],rev) 
                my_dict[f"{nums[i]},{[j]},{rev}"] = 1
                if f"nums[i],nums[j],rev" not in my_dict.keys():
                    k = nums.index(rev) 
                    if i != j and i != k and j != k :
                        out.append([nums[i],nums[j],rev])
    return out




if __name__ == "__main__":
    inputs = [[-1,0,1,2,-1,-4],[],[0]]
    for nums in inputs:
        print(f"Input : {nums}")
        print(f"Solution_1 : {solution(nums)}")
        print(f"Solution_2 : {solution_2(nums)}")



