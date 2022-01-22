class stack:
    def __init__(self):
        self.A = []
        
    def push(self,val):
        self.A.append(val)
        return val

    def pop_element(self):
        if len(self.A) == 0:
            print("Stack is empty ")
            return 
        return self.A.pop()

    def display(self):
        print(self.A)

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
    
    def postfix_evaluation(self,exp): 
        operators = ['+','-','*','/']
        for i in range(len(exp)):
            if exp[i] not in operators:
                my_stack.push(int(exp[i]))
            elif exp[i] in operators:
                value1 = self.pop_element()     
                value2 = self.pop_element()
                if exp[i] == '+':
                    my_stack.push(value2+value1)
                elif exp[i] == '-':
                    my_stack.push(value2-value1)    
                elif exp[i] == '*':
                    my_stack.push(value2*value1)
                elif exp[i] == '/':
                    my_stack.push(value2/value1)    
                else:
                    print("Invalid character")
                    return 
        return self.display()           

    def rev(self,val):
        if val == ')':return '('
        elif val == '}':return '{'
        elif val == ']':return '['

    def is_balanced(self,expr):
      
        parenthesis = ['(','{','[']
        for i in range(len(expr)):
            if expr[i] in parenthesis:
                self.push(expr[i])
            elif self.rev(expr[i]) in parenthesis:
                self.pop_element()
         
        if self.is_empty():
            return "Balanced"
        else:
            return "Not Balanced"                         

    def get_min(self):

        pass


if __name__ == "__main__":
    my_stack = stack()
    while(1):
        print("Enter choices ")
        print("1 : PUSH")
        print("2 : POP ")
        print("3 : PEEK")
        print("4 : LENGTH")
        print("5 : POSTFIX_EXPRESSION")
        print("6 : IS_BALANCED")
        n = int(input())
        if n == 1:
            val = int(input("Enter the value to push "))
            my_stack.push(val)
            my_stack.display()

        elif n == 2:
            my_stack.pop_element()
            my_stack.display()
        elif n == 3:
            print(f"Peek : {my_stack.peek()}")    
        elif n == 4:
            print(f"Size of stack is : {my_stack.count()}")
        elif n == 5:
            my_stack = stack()
            expr = input("enter the expression")
            print(my_stack.postfix_evaluation(expr))  
        elif n == 6:
            my_stack = stack()
            expr = input("Enter the expression")
            print(my_stack.is_balanced(expr))      
        else:
            exit(-1) 

