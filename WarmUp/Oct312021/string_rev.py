"""
Given as string array , reverse it without using any lib 
"""
# Approach 1 : Python tricks ( advantageous python )
def solution_1(input_str):
    return (input_str[::-1])

# Approach 2 : Using other array O(n)
def solution_2(input_str):
    n = len(input_str)
    temp = ""
    for i in range(n-1,-1,-1):
        temp = temp+input_str[i]
    return (temp)    

# Approach 3 : Without using external array 
# Two pointer approach 
# Python doesn't support string assignments as string are immutable 
# string -> list -> logic -> rev_list -> string 

def solution_3(input_str):
    n = len(input_str)
    start , end = 0 , n-1
    str_list = []
    for i in input_str:
        str_list.append(i)

    while start < end :
        str_list[start],str_list[end] = str_list[end],str_list[start]
        start += 1
        end -= 1

    strr = ""    
    for i in str_list:
        strr = strr + i

    return strr

# Approach 4 : Two pointer Approach 
# Tranverse through half approach    

# Not working .. try again 
def solution_4(input_str):
    n = len(input_str)
    m = int(n/2)
    my_list = []
    for i in input_str:
        my_list.append(i)

    for i in range(m-1):
        my_list[m-i],my_list[m+i] = my_list[m+i],my_list[m-i]
    return my_list     
   
# Tranverse through half approach      


if __name__ == "__main__":
    input_string = ["hello","mukesh","paridhi"]
    for my_str in input_string:
        rev = solution_1(my_str)
        print(f"Solution 1 : {my_str} =>  {rev} ")
        rev = solution_2(my_str)
        print(f"Solution 2 : {my_str} => {rev}")
        rev = solution_3(my_str)
        print(f"Solution 3 : {my_str} => {rev}")
        rev = solution_4(my_str)
        print(f"Solution 4 : {my_str} => {rev}")