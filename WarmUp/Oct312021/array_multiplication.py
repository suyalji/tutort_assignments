"""
Input :  2,3,4,5,6
output : 2.3 , 2.4, 3.5 , 4.6 , 5.6
          6, 8 , 15 , 24 , 30 


"""
# Brute Force   O(n)
arr = [2,3,4,5,6]
n = len(arr)
temp = [1]*n
for i in range(n):
    print(i)
    if i == 0:
        temp[i] = arr[i] * arr[i+1]
    elif i == n-1:
        temp[i] = arr[n-1] * arr[n-2]
    else:
        temp[i] = arr[i-1] * arr[i+1]
print (temp)         

# Optimised



