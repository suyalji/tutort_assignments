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