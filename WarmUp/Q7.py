"""
Q7. Given an array of length N, at each step it is reduced by 1 element. In the first step the maximum
element would be removed, while in the second step minimum element of the remaining array would
be removed, in the third step again the maximum and so on. Continue this till the array contains only 1
element. And find the final element remaining in the array.
"""
def find_max(arr):
    max = arr[0]
    for i in range(1,len(arr)):
        if arr[i] > max:
            max = arr[i]
    return max     
def find_min(arr):
    min = arr[0]
    for i in range(1,len(arr)):
        if arr[i] < min:
            min = arr[i]
    return min            

if __name__ == "__main__":            
    n = int(input())
    A = list(map(int,input().split()))
    i = 0
    while(len(A)>1):
        i += 1
        if i%2 != 0:
            A.remove(find_max(A))
        else:
            A.remove(find_min(A)) 
    for i in A:          
        print(i)

