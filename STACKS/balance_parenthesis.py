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
