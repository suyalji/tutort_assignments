"""
Q7. Given an array of length N, at each step it is reduced by 1 element. In the first step the maximum
element would be removed, while in the second step minimum element of the remaining array would
be removed, in the third step again the maximum and so on. Continue this till the array contains only 1
element. And find the final element remaining in the array.
"""
def debug(s):
    print(f"debug : {s}")
def sort(arr):
    for i in range(len(arr)):
        temp = arr[i]
        debug(f"1 -> {temp}")
        for j in range(i+1,len(arr)):
            if arr[j] < temp:
                arr[j],temp = temp,arr[j] # swap
                debug(f"2 -> {arr[j]}")
                debug(f"3 -> {temp}")
    return arr        
            
n = int(input())
A = list(map(int,input().split()))

print(A)
print(sort(A))