# 1
class Solution(object):
    def moveZeroes(self, nums):
        for i in nums:
            if i == 0 :
                nums.remove(i)
                nums.append(0)
                
# 2 
class Solution(object):
    def containsDuplicate(self, nums):
        n1 = len(nums)
        n2 = len(set(nums))

        if n1 != n2:
            return True
        else:
            return False

# 3
def solution_3(nums,k): # Time Limit Exceeded 
    n = len(nums)
    my_dict = {}
    for i in range(n):
        if nums[i] in my_dict.keys() and i - my_dict[nums[i]] <= k:
            return True
        else:
            my_dict[nums[i]] = i 
    return False           

# 4
    
                            