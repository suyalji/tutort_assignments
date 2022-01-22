class Solution(object):
    def nextGreaterElement(nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        temp = []
        for i in nums1:
            if i in nums2:
                j = nums2.index(i)
                ind = 0
                for k in range(j+1,len(nums2)):
                    if (nums2[k] > i):
                        temp.append(nums2[k])
                        ind += 1
                        break
                if ind == 0 : temp.append(-1)
        return temp 
         





if __name__ == "__main__":
    nums1 = [4,1,2]
    nums2 = [1,3,4,2]
    print(Solution.nextGreaterElement(nums1,nums2))
    nums1 = [2,4]
    nums2 = [1,2,3,4]
    print(Solution.nextGreaterElement(nums1,nums2))
    nums1 = [1,3,5,2,4]
    nums2 = [6,5,4,3,2,1,7]
    print(Solution.nextGreaterElement(nums1,nums2))


