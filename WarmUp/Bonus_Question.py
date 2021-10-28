"""Given an array of even size N, task is to find minimum value that can be added to an element so that
array become balanced. An array is balanced if the sum of the left half of the array elements is equal
to the sum of right half."""

def sum(arr,a,b):
    sum = 0
    for i in range(a,b):
        sum = sum + arr[i]
    return sum    
   
if __name__ == "__main__":
    inputs  = [[1,2,1,2,1,3],[1,5,3,2]]
    for arr in inputs:
        middle , left , right = 0 , 0 , 0 
        if len(arr)%2 == 0:
            middle = int(len(arr)/2)
            left = sum(arr,0,middle)  
            right = sum(arr,middle,len(arr))
        else:
            middle = len(arr)/2
            left = sum(arr,0,middle+1)
            right = sum(arr,middle+1,len(arr)) 
        value = abs(left-right)    
        print(f"balancing value : {value}")    
    
