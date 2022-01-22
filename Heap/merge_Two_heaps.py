def merge_min_heap(heap1, heap2):
    combined = heap1 + heap2
    print(f"Combined Heap is :: {combined}")
    for item in range(len(combined)-1,-1,-1):
        heapify(combined,item)

    return combined 

def heapify(arr , index ):

    n = len(arr)
    smallest = index 
    left  = 2*index + 1
    right = 2*index + 2

    if left < n and arr[left] < arr[smallest]:
        smallest = left 

    if right < n and arr[right] < arr[smallest]:
        smallest = right 

    if smallest != index:
        arr[smallest] , arr[index] = arr[index],arr[smallest]
        heapify(arr, smallest)        


if __name__ == "__main__":
    heap_1 = [1, 7, 4, 6, 10, 11]
    heap_2 = [13, 12, 2, 15, 16, 9]

    new_heap = merge_min_heap(heap_1,heap_2)

    print(f"Merged Heap is :  {new_heap}")

