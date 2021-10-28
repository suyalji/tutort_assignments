# 1: Given an array of N integers. Your task is to print the sum of all of the integers
import os

if __name__ == "__main__":
    n = int(input())
    a = list(map(int,raw_input().split()))
    sum = 0
    for i in a:
        sum = sum+i
    print(sum)


