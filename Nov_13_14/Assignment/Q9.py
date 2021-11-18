""" 
Given an integer array of size n, find all elements that appear more than ⌊ n/3 ⌋ times.
"""

def solution(nums):
    n = len(nums)
    my_dict = {}
    for i in nums:
        if i in my_dict.keys():
            my_dict[i] = my_dict[i] +1
        else:
            my_dict[i] = 1    
    out = []        
    for key,value in my_dict.items():
        if value > int(n/3):
            out.append(key)
    return out        

if __name__ == "__main__":
    inputs = [[3,2,3],[2,2,1,1,1,2,2],[1],[1,2]]
    for arr in inputs:
        print(f"Input : {arr}")
        print(f"Solution : {solution(arr)}")
