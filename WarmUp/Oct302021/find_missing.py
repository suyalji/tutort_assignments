"""
An array is given of range (1,n) , one element is missing find that . Missing element is represented by 0
"""
# Approach 1
def solution_1(arr):
    n = len(arr)
    for i in range(n):
        if i in arr:
            pass
        else:
            return i 

# Approach 2  - Direct formula : Sum of n nums
def solution_2(arr):
    n = len(arr)
    sum_array = 0
    for i in arr:
        sum_array = sum_array + i
    sum_n = n*(n+1)/2    
    return int(sum_n - sum_array)

# Approach 3 - Advantageous python , direct function 
def solution_3(arr):
    n = len(arr)
    sum_array = sum(arr)
    sum_n = n*(n+1)/2    
    return int(sum_n - sum_array)

# Approach 4 - Use boolean array 
def solution_4(arr):
    n = len(arr)
    temp = [0]*n  # Boolean array having all zero [0,0,0,0.....]
    for i in arr:
        temp[i-1] = 1
    for i in range(len(temp)):
        if temp[i]== 0:
            return i+1

# Driver code  
if __name__ == "__main__":
    arr = [1,2,3,5,0]
    missing = solution_1(arr)
    print(f"MISSING_1 : {missing}")
    missing = solution_2(arr)
    print(f"MISSING_2 : {missing}")
    missing = solution_3(arr)
    print(f"MISSING_3 : {missing}")
    missing = solution_4(arr)
    print(f"MISSING_4 : {missing}")
