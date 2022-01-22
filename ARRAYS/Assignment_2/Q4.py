def solution(arr):
    out = []
    range_str = ""
    start = 0
    for i in range(len(arr)-1):
        print(f"start,i , arr[i],arr[i+1]: {start}: {i} : {arr[i]} : {arr[i+1]}")

        if start == 0 and (arr[i+1] - arr[i] != 1):
            range_str = f"{arr[i]}"
            start = 0
            out.append(range_str)
        
        elif start == 0 and (arr[i+1] - arr[i] == 1):
            range_str = f"{arr[i]}->"
            start += 1    
        
        elif start > 0 and (arr[i+1] - arr[i] == 1):
            start += 1
            
        elif start > 0 and (arr[i+1] - arr[i] != 1):
            range_str = range_str+f"{arr[i]}"
            out.append(range_str)
            start = 0
    print(out)

def solution_2(arr):
    n = len(arr)
    out = []
    start = 0
    range_str = ''
    for i in range(1,n):
        
        if start == 0 and (arr[i]-arr[i-1]!= 1) :
           range_str = f"{arr[i-1]}"
           out.append(range_str)
           start = 0
        
        elif start == 0 and (arr[i]-arr[i-1] == 1):
            start += 1   
            range_str = f"{arr[i-1]}->"
        
        elif start > 0 and arr[i]-arr[i-1] == 1:
            start += 1
        
        elif start > 0 and arr[i] - arr[i-1] != 1:
            range_str = range_str+f"{arr[i-1]}"
            out.append(range_str)
            start = 0
        print(out)

def final_solution(arr):
    start_index = 0 
    result = []
    
    for i in range(len(arr)):
        if i+1 < len(arr) and arr[i]+1 == arr[i+1]:
            continue
        if start_index == i:
            result.append(f"{arr[start_index]}")
        else:
            result.append(f"{arr[start_index]}->{arr[i]}")
        start_index += 1
    return result          

 
if __name__ == "__main__":
    input = [[0,1,2,4,5,7],[0,2,3,4,6,8,9,]]
    case = 0
    for arr in input:
        case += 1
        print(f"Case : {case}")
        print(final_solution(arr))