"""
Pascals Triangle row by Row index 
Accepted by Leet Code , though not looks optimal 
"""

def solution(rowIndex):
    out = []
    if rowIndex == 0:
        return [1]
    elif rowIndex == 1:
        return [1,1]
    else:                    
        for i in range(rowIndex+1):
            if i == 0 :
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
                if i == rowIndex:
                    return (temp)
                out.append(temp)
            
    #return out

if __name__ == "__main__":
    inputs = [0,1,2,3,4,5,6,10]
    for row in inputs:
         print(f"Row : {row}")
         print(f"Solution : {solution(row)}")