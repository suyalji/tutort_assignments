"""
Q5. Given an array Arr of N positive integers. Your task is to find the elements whose value is equal
to that of its index value ( Consider 1-based indexing ).
"""

n = int(input())
arr = list(map(int,input().split()))

for i in range(0,n):
    if i+1 == arr[i]:
        print(arr[i])