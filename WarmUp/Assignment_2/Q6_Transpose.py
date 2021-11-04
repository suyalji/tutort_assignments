""" 
Given a 2D integer array matrix, return the transpose of matrix.
The transpose of a matrix is the matrix flipped over its main diagonal, switching the matrix's row and column indices.
"""
def solution_1(arr):
    n =len(arr)
    print(f"length = {n}") 
    for i in arr:
        for j in range(len(i)):
            arr[i][j],arr[j][i]= arr[j][i],arr[i][j]
    return arr
  

if __name__ == "__main__":
    inputs = [ [[1,2,3],[4,5,6],[7,8,9]],[[1,2,3],[4,5,6]]]
    for arr in inputs:
        print(f"Solution_1 : {solution_1(arr)}")

