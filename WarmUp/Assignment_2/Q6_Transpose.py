""" 
Given a 2D integer array matrix, return the transpose of matrix.
The transpose of a matrix is the matrix flipped over its main diagonal, switching the matrix's row and column indices.
"""
def solution_1(arr):
   
    n =len(arr)
    m= len(arr[0])
    x = [] 
   
    for i in range(m):
        y = []
        for j in range(n):
            y.append(arr[j][i])
        x.append(y)    
    return x

def solution_3(arr):
   
    n =len(arr)
    m= len(arr[0])
    x = [] 
   
    for i in range(m):
        arr[i] = []
        for j in range(n):
            arr[i].append(arr[j][i])
           
    return arr    

def solution_2(X):
    X = [[X[j][i] for j in range(len(X))] for i in range(len(X[0]))]
    return X

if __name__ == "__main__":
    inputs = [ [[1,2,3],[4,5,6],[7,8,9]],[[1,2,3],[4,5,6]]]
    for arr in inputs:
        print(f"Solution_1 : {solution_1(arr)}")
        print(f"Solution_2 : {solution_2(arr)}")
        print(f"Solution_3 : {solution_3(arr)}")
        

          
