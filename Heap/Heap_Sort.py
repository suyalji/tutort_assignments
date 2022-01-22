def heapsort(arr,max=1):
    n = len(arr) - 1
    # First Construct a Max Heap 
   
    for i in range(n , -1 , -1):
        Heapify(arr, i,max)
    
    print(f"After Heapify : {arr}")
    # Secondly pick root , and heapify 
    sort = []
    m = len(arr)
    while m > 0:
        sort.append(arr[0])
        arr.remove(arr[0])
        n = m - 2
        for i in range(n , -1 , -1):
            Heapify(arr, i,max)

        m = len(arr)    
    return sort         

def Heapify(arr, index , max = 1):
    n = len(arr)

    minimum = index
    maximum = index
    left  = 2*index + 1
    right = 2*index + 2

    if max == 1:     
        if left < n and arr[left] > arr[maximum]:
            maximum = left

        if right < n and arr[right] > arr[maximum]:
            maximum = right

        if maximum != index:
            arr[maximum] , arr[index] = arr[index] , arr[maximum]
            Heapify(arr,maximum) 
    else:     
        if left < n and arr[left] < arr[minimum]:
            minimum = left

        if right < n and arr[right] < arr[minimum]:
            minimum = right

        if minimum != index:
            arr[minimum] , arr[index] = arr[index] , arr[minimum]
            Heapify(arr,minimum,0) 



if __name__ == "__main__":
    arr = [1, 2, 7, 3, 10, 8, 100, 150, 110]
    print(f"Given array is : {arr}")
    arr = heapsort(arr,0)
    print(f"After Ascending Sort : {arr}")
      
    print(f"After Decending Sort : {heapsort(arr)}")