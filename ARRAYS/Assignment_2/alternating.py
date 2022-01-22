def alternating(A):
    a,b = 0,0
    for i in range(len(A)):
        
        m = i & 1^A[i]
        print(f"m = {m}")
        a,b = m+a,(not m) + b
       
        print(f"i:{i} || XOR: {1^A[i]} || m: {m} : a: {a} : b : {b}")
    
    return min(a,b)


if __name__ == "__main__":
    inputs = [[1,0,1,0,1,1]]
    for arr in inputs:
        print(alternating(arr))         