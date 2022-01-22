def minHeap(arr):
    n = len(arr) - 1
    for i in range(n, -1 , -1):
        heapify(arr,i)
    return arr    

def heapify(arr, index):
    n = len(arr)
    
    smallest = index
    left  = 2*index + 1
    right = 2*index + 2

    # adjusting smallest with left  
    if left < n and arr[left] < arr[smallest]:
        smallest = left
    
    # adjusting smallest with right 
    if right < n and arr[right] < arr[smallest]:
        smallest = right 
    
    if smallest != index:
        arr[smallest] , arr[index] = arr[index],arr[smallest]
        heapify(arr, smallest) 

def deleteHeap(arr):
    arr.remove(arr[0])
    n = len(arr) - 1
    for item in range(n , -1  , -1):
        heapify(arr,item)
    return arr 

def addMinHeap(arr , item):
    arr.append(item)
    n = len(arr) - 1
    for i in range(n , -1 , -1):
        heapify(arr, i)
    return arr 

if __name__ == "__main__":
    arr = [1, 4, 6, 5, 2, 9, 87, 76, 0]

    # Create a Min Heap 
    print(f"Min Heap is : {minHeap(arr)}")

    print("Adding new element ..")
    new_item = int(input("Enter a number to be added "))
    print(f"The Heap after addition is : {addMinHeap(arr,new_item)}") 


    print("Deleting element .. ")
    print(f"Heap after deleting is : {deleteHeap(arr)}")