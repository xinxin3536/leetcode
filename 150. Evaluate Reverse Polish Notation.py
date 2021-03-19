class Solution:
   
    def isNum(self,cc:str) -> bool:
        if cc == '+' or cc == '-' or cc == '*' or cc == '/':
            return False
        else:
            return True
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for i in tokens:
                if self.isNum(i):
                     stack.append(int(i))
                else:
                    a = stack.pop(-1)
                    b = stack.pop(-1)
                    if i == '+':
                        c = a + b
                        stack.append(c)
                        
                    elif i == '-':
                        c = b - a
                        stack.append(c)
                    elif i == '*':
                        c = b * a
                        stack.append(c)
                    elif i == '/':
                        c = b / a
                        stack.append(int(c))
        return stack[0]

            

