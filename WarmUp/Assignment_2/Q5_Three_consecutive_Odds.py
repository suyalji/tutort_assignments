"""
Given an integer array arr, return true if there are three consecutive odd numbers in the array. Otherwise, return false.
"""
def solution_1(arr): # Not part of this assignment 
    n = len(arr)
    for i in range(n-3):
        if arr[i+1]-arr[i] == arr[i+2]-arr[i+1] == 1:
            return True
    return False

def solution_2(arr):
    n = len(arr)
    for i in range(n-2):
        if arr[i]%2 != 0 and arr[i+1]%2 != 0 and arr[i+2]%2 != 0 :
            return True 
    return False

if __name__ == "__main__":
    inputs = [[2,6,4,1],[1,2,34,3,4,5,7,23,12],[1,1,1]]
    for arr in inputs:
        print(f"Solution_1 :  {solution_1(arr)}")
        print(f"Solution_2 :  {solution_2(arr)}")

        