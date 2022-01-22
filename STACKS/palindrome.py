def solution_1(arr):
    # Two Pointer Approach
    n = len(arr)
    start , last  = 0 , n-1 

    while(start < last):
        if arr[start] != arr[last]:
            print("Not Palindrome")
            return 0
        start += 1
        last -= 1
    print("Palindrome")    
    return 1    

class stack:
    def __init__(self):
        self.A = []
    def push(self,data):
        return self.A.append(data)    
    def pop(self):
        return self.A.pop()
    def display(self):
        print(self.A)    
    def peak(self):
        return self.A[-1]    
    def palindrome(self,str):
        n = len(str)
        middle = int(n/2)
        
        my_stack = stack()
        num = 0 
        
        while num < middle:
            my_stack.push(str[num])
            num += 1
        
        if middle %2 != 0:
            num += 1
        
        while num < n:
            if str[num] == my_stack.peak():
                my_stack.pop()
                num += 1
            else:
                print("Not Palindrome")
                return 0
        print("Palindrome")
        return 1



if __name__ == "__main__":  
    abc = stack()
    abc.push(5)
    abc.push(7)
    abc.display()
    abc.pop()
    abc.display()
    print(abc.peak())
    inputs = ["mom","Tom","Dad","Monket","MonkeyyeknoM"]
    for bb in inputs:
        print("Two Pointer Approach")
        solution_1(bb)
        print("Stack Approach")
        abc.palindrome(bb)
        print("-----------------------------")
"""





    

def solution_2(arr):
    n = len(arr)
    middle = n/2

    A = []
    count = 0
    while count < middle:
        A.append[arr[count]]
        count += 1
    while len(A) != 0:
        if A[count] == A[-1]:
            A.pop()
            
        else:
            print("Not palindrome")
            return 0         


if __name__ == "__main__":
    inputs = ['mom','dad','mukesh','marbbramm']
    for arr in inputs:
        print("Two Pointer Approach ")
        solution_1(arr)
        print("Stack Approach ")
        solution_2(arr) 

        """