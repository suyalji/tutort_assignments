arr = [100,1,11,1,120,111,123,1,-1,-100]
n = len(arr)
final = [-1]*n
arr2 = arr

def nextGreaterElements(nums):
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
    print(final)        