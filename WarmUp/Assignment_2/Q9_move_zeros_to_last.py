""" 
Given an integer array nums, move all 0's to the end of it while maintaining the relative order of the non-zero elements.
Note that you must do this in-place without making a copy of the array.
"""
def solution_1(arr):  # Brute Force O(n2)
    n = len(arr)
    for i in range(n-1):
        for j in range(i+1,n):
            if arr[i] == 0:
                 arr[i],arr[j] = arr[j],arr[i]
    return arr        

def solution_2(arr):
    for i in arr:
        if i == 0:
            arr.remove(i)
            arr.append(0)
    return arr

if __name__ == "__main__":
    inputs = [[0,1,0,3,12],[0]]
    for arr in inputs:
        print(f"Solution_1 : {solution_1(arr)}")
        print(f"Solution_2 : {solution_2(arr)}")