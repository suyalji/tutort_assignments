"""
Given an array of distinct integers arr, find all pairs of elements with the minimum absolute difference of any two elements. 
Return a list of pairs in ascending order(with respect to pairs), each pair [a, b] follows
a, b are from arr
a < b
b - a equals to the minimum absolute difference of any two elements in arr
"""
import sys
def solution_1(arr):  # working but time complexity very high so rejected by LeetCode
    min = sys.maxsize
    out = []
    n = len(arr)
    for i in range(0,n-1):
        for j in range(i+1,n):
            diff = abs(arr[i] - arr[j])
            if diff < min:
                out = []
                min = diff  
                sort = sorted([arr[i],arr[j]])   
                out.append(sort)
            elif diff == min:
                sort = sorted([arr[i],arr[j]])   
                out.append(sort)
    return sorted(out)

def solution_2(arr):  ## Accepted by Leetcode
    out,n = [],len(arr)
    arr = sorted(arr)
    my_dict = {}
    mini = sys.maxsize
    my_list = []
    for i in range(n-1):
        diff = abs(arr[i]-arr[i+1])
        if diff < mini:
            mini = diff
            my_list = []
            my_list.append([arr[i],arr[i+1]])
        elif diff == mini:
            my_list.append([arr[i],arr[i+1]])    
    return my_list

if __name__ == "__main__":
    inputs = [[4,2,1,3],[1,3,6,10,15],[3,8,-10,23,19,-4,-14,27],[-169,-133,178,-50,-4,138,136,-140,137,69,8,-80,3,183,-57,164,192,191]]
    for arr in inputs:
        result = solution_1(arr)
        print(f"Soltion_1 : {result}")
        result = solution_2(arr)
        print(f"Solution_2 : {result}")
        