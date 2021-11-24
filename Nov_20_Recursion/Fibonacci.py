def fibbo_with_recursion(n):
    my_list = []
    if n <0:
        print("incorrect input")
    elif n == 0:
        my_list.append(0)
        return 0
    elif n == 1:
        my_list.append(1)
        return 1
    else :
        k =  fibbo_with_recursion(n-1) + fibbo_with_recursion(n-2)
        my_list.append(k)
        return k
    return my_list
    
def fibbo_without_recursion(n):
    my_list = [] 
    if n == 0:
        my_list.append(0)
    elif n == 1:
         my_list.append(1)
    else :
        my_list.append(0)
        my_list.append(1)     
    for i in range(2,n):
        sum = my_list[i-1] + my_list[i-2] 
        my_list.append(sum)
    return my_list            
        
if __name__ == "__main__":
    inputs = [0,1,2,3,4,5,10]
    for n in inputs:
        print("--------------------------------------------------")
        print("Without Recursion")
        print(f"n =  {n} : {fibbo_without_recursion(n)}")
        print("With Recursion")
        print(f"n =  {n} : {fibbo_with_recursion(n)}")
        print("--------------------------------------------------")