""" HARD
Given array represents water bars , we need to find the Total water trapped combining all bars  
Understanding :
               1.  Sorted array will not able to store any water 
               2.  Zeroes in beginning or end will serve no purpose
               3.  All elements in Array will be positive
               4.  Single element in Array traps no water
"""
def solution_1(arr):
    n = len(arr)
    for i in range(n):
        for j in range(i+1,n):
            mini = min(arr[i],arr[j])
            



if __name__ == "__main__":
    inputs = [[0,1,0,2,1,0,3,1,0,1,2],[4,3,2,1,2,3,4],[1,2,3,4,5],[5,4,3,2,1],[5,4,3,2,1,2,0]]
    case = 0
    for arr in inputs:
        case += 1
        print(f"Case : {case}")
        print(f"Input : {arr}")
        print(f"Output : {solution_1(arr)}")
        print("--------------------------------------------------------")
