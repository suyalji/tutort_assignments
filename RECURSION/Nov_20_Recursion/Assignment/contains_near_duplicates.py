def solution_brute_force(nums,k): # Brute Force
    n = len(nums)
    for i in range(n):
        for j in range(i+1,n):
            if (nums[i] == nums[j]) and (abs(i-j)<=k):
                return True
    return False            


def solution_2(nums,k): # Time Limit Exceeded 
    n = len(nums)
    my_dict = {}
    for i in range(n):
        if nums[i] in my_dict.keys():
            sum = abs(i - my_dict[nums[i]])
            if sum <= k:
                return True
            else:
                my_dict[nums[i]] = i    
        else:
            my_dict[nums[i]] = i
    return False

def solution_3(nums,k): # Time Limit Exceeded 
    n = len(nums)
    my_dict = {}
    for i in range(n):
        if nums[i] in my_dict.keys() and i - my_dict[nums[i]] <= k:
            return True
        else:
            my_dict[nums[i]] = i 
    return False             




if __name__ == "__main__":
    inputs = [[1,2,3,1],[1,0,1,1],[1,2,3,1,2,3]]
    kk = [3,1,2]
    for i in range(len(inputs)):
        print("-------------------------------------")
        print(solution_brute_force(inputs[i],kk[i]))
        print(solution_2(inputs[i],kk[i]))
        print(solution_3(inputs[i],kk[i]))
        print("......................................")