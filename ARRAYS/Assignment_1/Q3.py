""" 
You are given two integer arrays nums1 and nums2, sorted in non-decreasing order, and two integers m and n, representing the number of elements in nums1 and nums2 respectively.
Merge nums1 and nums2 into a single array sorted in non-decreasing order.
The final sorted array should not be returned by the function, but instead be stored inside the array nums1. To accommodate this, nums1 has a length of m + n, where the first m elements denote the elements that should be merged, and the last n elements are set to 0 and should be ignored. nums2 has a length of n.
Example 1:
Input: nums1 = [1,2,3,0,0,0], m = 3, nums2 = [2,5,6], n = 3
Output: [1,2,2,3,5,6]
Explanation: The arrays we are merging are [1,2,3] and [2,5,6].
The result of the merge is [1,2,2,3,5,6] with the underlined elements coming from nums1.
Example 2:
Input: nums1 = [1], m = 1, nums2 = [], n = 0
Output: [1]
Explanation: The arrays we are merging are [1] and [].
The result of the merge is [1].
Example 3:
Input: nums1 = [0], m = 0, nums2 = [1], n = 1
Output: [1]
Explanation: The arrays we are merging are [] and [1].
The result of the merge is [1].
Note that because m = 0, there are no elements in nums1. The 0 is only there to ensure the merge result can fit in nums1.
Constraints:
nums1.length == m + n
nums2.length == n
0 <= m, n <= 200
1 <= m + n <= 200
-109 <= nums1[i], nums2[j] <= 109
Follow up: Can you come up with an algorithm that runs in O(m + n) time?
"""
def solution(nums1,nums2,m,n):
    """ 
    This solution works well in my local system but failing for one case in Leetcode
    nums1 = [0],m=0,nums2=[1],n=1
    Can some one help here ? 
    """
    if m == 0:
        nums1 = nums2
        return nums1
      
    mn = len(nums1)-1
    m = m-1
    n = n-1
   
    for i in range(mn,1,-1):
        if nums1[m] <= nums2[n]:
                nums1[i] = nums2[n]
                n -= 1
        elif nums1[m] > nums2[n]:
                nums1[i] = nums1[m]
                m -= 1
    return nums1         
                 
def merge(nums1, m, nums2, n):
        while m > 0 and n > 0:
            if nums1[m-1] >= nums2[n-1]:
                nums1[m+n-1] = nums1[m-1]
                m -= 1
            else:
                nums1[m+n-1] = nums2[n-1]
                n -= 1
        if n > 0:
            nums1[:n] = nums2[:n]
        return nums1


if __name__ == "__main__":
    nums1 = [1,2,3,0,0,0]
    nums2 = [2,5,6]
    m,n=3,3
    print(f"Solution : {solution(nums1,nums2,m,n)}")
    nums1 = [1]
    nums2 = []
    m,n=1,0
    print(f"Solution : {solution(nums1,nums2,m,n)}")
    nums1 = [0]
    nums2 = [1]
    m,n=0,1
    print(f"Solution : {solution(nums1,nums2,0,1)}")
    print(f"solution_ : {merge(nums1, m, nums2, n)}")
 

    #print(shift1(nums1,1))