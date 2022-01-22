"""
Find the number of ways to find the total sum value 
using the range 1 to k
Solved - using knapsack 0/1
"""
def solution(total,k):
   #total = int(input())
   #k = int(input())
    total = 5
    k = 3
   ## making an array of size [k+1][total+1] 
    arr = [[0 for y in range(total+1)]for x in range(k+1)]

    for i in range(total+1):
         arr[0][i] = 0
         arr[1][i] = 1
    print(arr)
    
    for i in range(k+1):
       arr[i][0] = 0
    print("\n-----------------\n")   
    print(arr)

    for row in range(2,k+1):
        for col in range(1,total+1):
            if col < row:
                arr[row][col] = arr[row-1][col]
            elif col == row:
                arr[row][col] = arr[row-1][col] + 1
            else:
                arr[row][col] = arr[row-1][col]  +  arr[row][col-row]
    print(arr)
    print(arr[k][total])



if __name__ == "__main__":
    total,k = 5,3
    solution(total,k)