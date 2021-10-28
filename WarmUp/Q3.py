"""
Q3. Given an sorted array A of size N. Find number of elements which are less than or equal to given
element X.
"""
n = int(input())
a = list(map(int,raw_input().split()))
x = int(input())

count = 0
for i in a:
    if i <= x:
        count+=1
print(count) 



