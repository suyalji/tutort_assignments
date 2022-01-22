def solution(A):
    ans = N = len(A)
    s = 0
    for i in range(2 * N):
        s += int(A[i % N]) ^ (i & 1)
        if i >= N - 1:
            ans = min(ans, s, N - s)
            s -= int(A[(i - (N - 1)) % N]) ^ ((i - (N - 1)) & 1)
    return ans

def minReplacement(s):
    length = len(s)
    ans = 0
    for i in range(0, length):
 
        # If there is 1 at even index positions
        if i % 2 == 0 and s[i] == '1':
            ans += 1
 
        # If there is 0 at odd index positions
        if i % 2 == 1 and s[i] == '0':
            ans += 1
     
    return min(ans, length - ans)    

def minOperations(s):
        a = b = 0
        for i in range(len(s)):
            if i%2 ==0 :
                if s[i]=='0': a+=1
                else: b+=1
            else:
                if s[i]=='1': a+=1
                else: b+=1
        return min(len(s)-a,len(s)-b)    

def minOperations_2(s) :
        count = 0
        count1 = 0
        for i in range(len(s)):
            if i % 2 == 0:
                if s[i] == '1':
                    count += 1
                if s[i] == '0':
                    count1 += 1
            else:
                if s[i] == '0':
                    count += 1
                if s[i] == '1':
                    count1 += 1
        return min(count, count1)

def minOperations_3(s):
    starting_with_01 = '01'
    starting_with_10 = '10'
    diff_with_01,diff_with_10 = 0,0
    for i in range(len(s)):
        if starting_with_01[i%2] != s[i]:
            diff_with_01 += 1
        if starting_with_10[i%2] != s[i]:
            diff_with_10 += 1
    return min(diff_with_01,diff_with_10)             

def solution_final(A):
    # write your code in Python 3.6
        a, b = 0, 0
        for i in range(len(A)):
            m = i & 1 ^ A[i]
            a, b = m + a, (not m) + b
        return min(a, b)

def short(A):    
        flips = sum((n ^ i) & 1 for i, n in enumerate(A))
        return min(flips, len(A)-flips)

def my_solution(A):
    count_list = []
    count_1 = 0
    count_2 = 0 
    # considering starts with 1
    for i in range(len(A)):
        if i%2 == 0: #odd position 0 , 2 ,4 
            if A[i] == 0:
                pass
            else:
                count_1 += 1
        else:  # even position 1, 3 , 5
            if A[i] == 1:
                pass
            else:
                count_1 += 1    
    count_list.append(count_1)   
    for i in range(len(A)):
        if i%2 == 0: #odd position 0 , 2 ,4 
            if A[i] == 1:
                pass
            else:
                count_2 += 1
        else:  # even position 1, 3 , 5
            if A[i] == 0:
                pass
            else:
                count_2 += 1    
    count_list.append(count_2)
    return min(count_list)    









if __name__ == "__main__":
    inputs = [[1,0,1,0,1,1],[1,1,0,1,1],[0,1,0],[0,1,1,0]]
    for arr in inputs: 
        print("Solution_1")
        print(solution_final(arr))   
        #print("sol2")
        #print(minReplacement(arr)) 
        #print("sol3")
        #print(minOperations(arr))
        ##print("sol4")
        #print(minOperations_2(arr))
        #print("sol5")
        #print(minOperations_3(arr))
        print("My Solution _ 2 ")
        print(my_solution(arr))
        print("Solution 3")
        print(short(arr))


        