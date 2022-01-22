"""  ACCEPTED IN LEETCODE *************************
Design a DS which has PUSH , POP and GETMIN function defined in O(1)
PUSH 
POP
GETMIN
"""
class stack:
    def __init__(self):
        self.A = []
        self.min_stack = []
        
    def push(self,val):
        if self.is_empty():
            self.A.append(val)
            self.min_stack.append(val) 

        else:
            self.A.append(val)
            last_minimum = self.min_stack[-1]
            self.min_stack.append(min(val,last_minimum))       

        return val

    def pop(self):
        if len(self.A) == 0:
            return
        elif len(self.min_stack) == 0:
            return 
        else:    
            self.min_stack.pop()
            return self.A.pop()

    def display(self):
        if len(self.A) & len(self.min_stack) :
            print(f"Stack : {self.A}")
            print(f"Minimum : {self.min_stack[-1]}")
        return 
    def count(self):
        return len(self.A)    
    
    def peek(self):
        if len(self.A) != 0:
            return self.A[-1]

    def is_empty(self):
        if len(self.A) == 0:
            return 1
        else:
            return 0            
     
    def get_min(self):
        if len(self.min_stack) == 0:
            return
        return self.min_stack[-1]
 


if __name__ == "__main__":
    my_stack = stack()
    while(1):
        print("Enter choices ")
        print("1 : PUSH")
        print("2 : POP ")
        print("3 : PEEK")
        print("4 : LENGTH")
        print("5 : GET MINIMUM ")
        
        n = int(input())
        if n == 1:
            val = int(input("Enter the value to push "))
            my_stack.push(val)
            my_stack.display()

        elif n == 2:
            my_stack.pop()
            my_stack.display()
        elif n == 3:
            print(f"Peek : {my_stack.peek()}")    
        elif n == 4:
            print(f"Size of stack is : {my_stack.count()}")
        elif n == 5:
            print(my_stack.get_min())
         
        else:
            exit(-1) 




