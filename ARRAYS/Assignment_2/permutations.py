def solution(num):
    num = str(num)
    my_list = []
    for i in num:
        my_list.append(i)
    num = my_list    

    left = 0
    right = len(num)-1
    return permutations(num,left,right)

def permutations(num,left,right):
    if left == right :
        return num
    for i in range(left,right):
        print(i)
        num[left],num[right] = num[right],num[left]
        print(num)
        permutations(num, left+1, right)
        num[left],num[right] = num[right],num[left]
    return num    

if __name__ == "__main__":
    inputs = [121,12]
    for num in inputs:
        print(solution(num))