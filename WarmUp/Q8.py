"""Q8. Given an array of N distinct elements, the task is to find all elements in array except two greatest
elements in sorted order."""

def sort(arr):
    for i in range(0,len(arr)):
        mini = arr[i]
        for j in range(i+1,len(arr)):
            if arr[j] < mini:
                mini = arr[j]
                arr[i],arr[j] = arr[j],arr[i]
    return arr


if __name__ == "__main__":
    arr = list(map(int,input().split()))

    for i in range(len(sort(arr))-2):
        print(arr[i])              
