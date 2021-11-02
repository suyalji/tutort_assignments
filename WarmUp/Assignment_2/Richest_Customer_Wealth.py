"""
You are given an m x n integer grid accounts where accounts[i][j] is the amount of money the i​​​​​​​​​​​th​​​​ customer has in the j​​​​​​​​​​​th​​​​ bank. Return the wealth that the richest customer has.
A customer's wealth is the amount of money they have in all their bank accounts. The richest customer is the customer that has the maximum wealth.
"""
def solution_1(arr):
    maxi = []
    for i in arr:
        maxi.append(sum(i))
    return max(maxi)

if __name__ == "__main__":
    arr = [[2,8,7],[7,1,3],[1,9,5]]
    print(solution_1(arr))
    print(solution_2(arr))



