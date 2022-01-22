def minHeap(arr , index):
    n = len(arr)

    minimum = index 
    left  = index*2 + 1
    right = index*2 + 2

    if left < n and arr[minimum] > arr[left]:
        minimum = left

    if right < n and arr[minimum] > arr[right]:
        minimum = right 

    if minimum != index:
        arr[minimum], arr[index] = arr[index], arr[minimum]
        minHeap(arr, minimum)



if __name__ == "__main__":
    arr = [2, 66, 30, 5, 9, 10]
    print(f"Given Array : {arr}")
    n = len(arr) - 1
    for element in range(n, -1, -1):
        minHeap(arr , element)
    print(f"After Heapify : {arr}")    

    new_element = int(input("Enter a new element "))
    arr.append(new_element)
    for element in range(len(arr),-1,-1):
        minHeap(arr,element)
    print(f"After insertion : {arr}") 
