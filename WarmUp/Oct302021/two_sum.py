"""
arr is given , and a sum is given . Find the two number in arr which form the sum 
input  : [2, 7, 11, 5]
sum    : 9
output : 2,7
"""
# Approach 1 : Brute Force O(n2)
def solution_1(arr,target):
    n = len(arr)
    for i in range(n):
        for j in range(i+1,n):
            if arr[i]+arr[j] == target:
                return [i,j]
    return None

# Approach 2   less then O(n2)
def solution_2(arr,target): 
    n = len(arr)
    for i in range(n):
        value = target - arr[i]
        if value in arr:
            return i,arr.index(value)

# Driver code 
if __name__ == "__main__":
    arr,target = [2, 7, 11, 5],16
    pair = solution_1(arr,target)
    print(f"Solution_1 : {pair}")
    pair = solution_2(arr,target)
    print(f"Solution_2 : {pair}")