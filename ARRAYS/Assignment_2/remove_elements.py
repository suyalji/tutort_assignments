class Solution(object):
    def removeElement(nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        while val in nums:
            nums.remove(val)
        return nums    


if __name__ == "__main__":
   print(Solution.removeElement([0,1,2,2,3,0,4,2,2,2,2],2))        