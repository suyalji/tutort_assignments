""" 
In sorted Array find the Total count of any number 
"""


def solution_1(nums):
    my_dict = {}
    for i in nums:
        if i in my_dict.keys():
            my_dict[i] += 1
        else:
            my_dict[i] = 1
    return my_dict

def solution_2(nums):
    # Array is sorted 
    n = len(arr)
    count = 0
    prev = 0
    for i in range(n): 
        if i == 0:
            count = 1
            prev = nums[i] 
        elif nums[i] == prev:
            count += 1
        else:
            print(f"Solution_2 => {nums[i]} : {count}")
            count = 0
          



if __name__ == "__main__":
    inputs = [[1,2,3,3,4,5,5,5,6],[1,1,1]]
    i = 0
    for arr in inputs:
        i+=1
        print(f"Case {i+1}")
        print(f"Solution : {solution_1(arr)}")
        print(f"Solution_2 : {solution_2(arr)}")
