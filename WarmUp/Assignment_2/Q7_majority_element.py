"""
Given an array nums of size n, return the majority element.
The majority element is the element that appears more than ⌊n / 2⌋ times. You may assume that the majority element always exists in the array.
"""
def solution_1(arr):
    n = len(arr)
    my_dict = {}
    for i in arr:
        if i in my_dict.keys():
            my_dict[i] = my_dict[i] + 1
        else:
            my_dict[i] = 1
    for key,value in my_dict.items():
        if value > int(n/2):
            return key        
    return None
    
if __name__ == "__main__":
    inputs = [[3,2,3],[2,2,1,1,1,2,2],[6,5,5]]
    for arr in inputs:
        print(f"Solution_1 : {solution_1(arr)}") 
