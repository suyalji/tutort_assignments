""" 
Parent Node = index/2
Left Child = 2*index + 1
Right Child = 2*index + 2


"""
def buildMinHeap(arr):
    n = len(arr)-1
    for i in range(n, 0, -1):
        print(f"Value  : {arr[i]}")
        heapify(arr , i)
        print("Step : ",arr)
        print("--------------------------")

def heapify(arr , index):
    n = len(arr)
    smallest = index
    left  = 2*index + 1
    right = 2*index + 2

    if left < n and arr[left] < arr[smallest]:
        smallest = left 

    if right < n and arr[right] < arr[smallest]:
        smallest = right 

    if smallest != index:
        arr[index],arr[smallest] = arr[smallest],arr[index]         

        heapify(arr,smallest)




if __name__ == "__main__":
    arr = [1, 5, 6, 8, 9, 7, 3]
    
    print("Array is ", arr)

    buildMinHeap(arr)

    print("After Heapify ", arr)
