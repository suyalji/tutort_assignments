"""
 Q2. Given an array A[] of N integers and an index Key. Your task is to print the element present at
index key in the array.
"""
import os

if __name__ == "__main__":

    a = list(map(int,raw_input().split()))
    b = list(map(int,raw_input().split()))
    n = a[0]
    index=a[1]
    print(b[index])