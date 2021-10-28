"""
Q4. You are given an array A of size N. You need to print elements of A in alternate order (starting
from index 0).
"""
n = int(input())
a = list(map(int,input().split()))

for i in range(0,n):
    if i %2 == 0:
        print(a[i],end=' ') 