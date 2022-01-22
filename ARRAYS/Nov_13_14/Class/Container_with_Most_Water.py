def solution(arr):
    # If we are not considering obstructions
    n = len(arr)
    start = 0
    end = n-1 
    max = -1
    while(start < end ):
        print("start,end :",start,end)
        length = min(arr[start],arr[end])
        breadth = end-start
        area = length*breadth
        if area > max:
            max = area
        if arr[start] < arr[end]:   
            start += 1
        else:     
            end -= 1   
    return max   


if __name__ == "__main__":
    inputs = [[7,1,2,9,3],[7,1,2,9,11]]
    for arr in inputs:
        print(solution(arr))
