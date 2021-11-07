"""
arr = [1, -3, 2, -5, 7]
output : subarry having maximum sum consequitive
"""
# Approach 1 
# Complexity = O(n)*O(n-1) =~ O(n2)
import sys 
def find_max(arr):
    n = len(arr)
    current_maximum = arr[0] # better any number from list
    for i in range(n):
        sum = 0
        for j in range(i,n):
            sum = sum + arr[j]
            if sum > current_maximum:
                current_maximum = sum
    return current_maximum 

# Approach 2
# Complexity O(n)
def solution_2(arr):  
    maxsum , sum = 0,0
    maxnegative = -sys.maxsize-1 
    for i in range(len(arr)):
        if arr[i]+sum > 0:
            sum += arr[i]
        else:
            sum = 0    
        if sum > maxsum:
            maxsum = sum 
        if arr[i] > maxnegative:
            maxnegative = arr[i]
    if maxsum ==0:
        return maxnegative
    else:    
        return maxsum                
   
if __name__ == "__main__":
  
    list_arr = [[1, -3, 2, -5, -9],[-2, -3, 4, -1, -2, 1, 5, -3],[0],[1, -3, 2, 5, -9],[1,-3,2,5,1],[-1,-2,-3,-4]]
    for arr in list_arr:
        print(f"Input : {arr}")
        max_sum = find_max(arr)
        print("solution_1",max_sum)
        max_sum = solution_2(arr)
        print("solution_2",max_sum)


