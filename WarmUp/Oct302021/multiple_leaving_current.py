"""
Given array , generate a product of all elements leaving the current 
Note : Please check boundary condition as well
"""
# Approach 1
def solution_1(arr):
    n = len(arr)
    prod = 1
    count = 0
    for i in arr:
        if i == 0:
            i =1 
            count+= 1 
        prod = prod * i    
    
    if count >= 2:
        return [0]*n
    
    for i in range(len(arr)):
        if arr[i] == 0:
            arr = [0]*n
            arr[i] = prod
        else:    
            arr[i] = int(prod/arr[i])
    return arr        

# Approach 2
def solution_2(arr):
    b,n = [],len(arr)
    for i in range(n):
        prod = 1
        for j in range(0,n):
            if i != j:
                prod = prod * arr[j]
        b.append(prod)
    return b

# Approach 3
def solution_3(arr):
    n = len(arr)
    left , right = [1]*n,[1]*n 
    left[0] = 1
    right[n-1] = 1

    for i in range(1,n):
        left[i] = left[i-1]*arr[i-1]

    for i in range(n-2,0):
        right[i] = right[i+1]*arr[i+1]

    print(f"left : {left}")
    print(f"right : {right}")
    
    for i in range(n):
        arr[i] = left[i] * right[i]
    
    return arr     



# Driver code
if __name__ == "__main__":
    arr = [1,2,3,4,5,6,4]
    product = solution_1(arr)
    print(f"Solution_1 : {product}")
    arr = [1,2,3,4,5,6,4]
    product = solution_2(arr)
    print(f"Solution_2 : {product}")
    arr = [1,2,3,4,5,6,4]
    product = solution_3(arr)
    print(f"Solution_3 : {product}")

