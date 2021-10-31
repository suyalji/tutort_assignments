"""
arr = [1, -3, 2, -5, 7]

output : subarry having maximum sum consequitive
"""
# Approach 1 
# Complexity = O(n)*O(n-1) =~ O(n2)
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
   
if __name__ == "__main__":
  
    list_arr = [[1, -3, 2, -5, -9],[-2, -3, 4, -1, -2, 1, 5, -3],[0],[1, -3, 2, 5, -9]]
    for arr in list_arr:
        print(f"Input : {arr}")
        max_sum = find_max(arr)
        print(max_sum)


