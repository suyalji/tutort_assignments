"""
Q6. Given an array of size N and you have to tell whether the array is perfect or not. An array is said
to be perfect if it's reverse array matches the original array. If the array is perfect then print
"PERFECT" else print "NOT PERFECT".
"""
import sys 

arr = list(map(int,input().split()))
first,last = 0,len(arr)-1 

while first<last: 
    if arr[first] == arr[last]:
        first+=1
        last-=1
    else:
        print("NOT PERFECT")
        sys.exit(-1)
print("PERFECT")
