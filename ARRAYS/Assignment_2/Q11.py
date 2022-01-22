class Solution(object):
    def nextGreaterElements_2(nums):  # Working but Timeout Error 
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        my_list = []
        n = len(nums)
        for i in nums:
            #print(f"i = {i}")
            index = nums.index(i)
                       
            m = index+1
            ind = 0
            cycle = 0
            while m != index and ind == 0: 
                
                if m >= n:
                    m = m%n
                    cycle = 1 
                if nums[m] > i:
                    my_list.append(nums[m])
                    ind = 1
                else:
                    m+=1
                
            if m == index  and ind == 0:
                    my_list.append(-1)

        return my_list

   

    def nextGreaterElements(nums):    ## Finally Succeded 
        n = len(nums)
        final = [-1]*n
        for i in range(len(nums)):
            j = i+1
            done = 0
            while j<n and done == 0:
                if nums[i] < nums[j]:
                    final[i] = nums[j]
                    done = 1     
                    break        
                else: j += 1
            k = 1
            if done == 0 : k = 0
            while k < i and done == 0:
                if nums[k] > nums[i]:
                    final[i] = nums[k]
                    done = 1 
                    break
                else: k += 1
        return final        
        


if __name__ == "__main__":
    inputs = [[1,2,3,4,3],[1,2,1],[1,2,3,4,5],[100,1,11,1,120,111,123,1,-1,-100]]
    for arr in inputs:
        print(Solution.nextGreaterElements(arr))
        print(Solution.nextGreaterElements_2(arr))


