"""
Pascals Triangle
Accepted by Leet Code 
"""

def solution(numRows):
    out = []
    for i in range(numRows):
        if i == 0:
            out.append([1])
        if i == 1:
            out.append([1,1])    
        if i >= 2:
            temp = []
            for j in range(i+1):
                if j == 0 or j == i:
                    temp.append(1)
                else:
                    sum = out[i-1][j-1] + out[i-1][j]
                    temp.append(sum)    
            out.append(temp)
    return out

if __name__ == "__main__":
    inputs = [1,2,3,4,5,6,10]
    for row in inputs:
         print(f"Row : {row}")
         print(f"Solution : {solution(row)}")