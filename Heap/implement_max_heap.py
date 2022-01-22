def Maxheapify(arr , n , index):
    largest = index
    left    = 2*index + 1
    right   = 2*index + 2


    #largest so far is compared with left child 
    if left < n and arr[largest] < arr[left]:
        largest = left

    #largest so far is compared with right child 
    if right < n and arr[largest] < arr[right]:
        largest = right 

    #change the parent 
    if largest != index:
        arr[index], arr[largest] = arr[largest], arr[index]
        #recursive call 
        Maxheapify(arr, n, largest)    


if __name__ == "__main__":
    arr = [2, 66, 30, 5, 9, 10]
    n = len(arr)

    # Build a Max Heap 
    for i in range(n//2-1, -1, -1):
        Maxheapify(arr,n,i)   

    # display 
    print("Max Heap is " , arr)    