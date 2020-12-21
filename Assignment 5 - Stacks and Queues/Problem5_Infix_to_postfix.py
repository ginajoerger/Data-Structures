# Use this stack to perform infix to postfix. No need to modify the stack class.
class ArrayStack:
    def __init__(self):
        self._data = []

    def __len__(self):
        return len(self._data)

    def is_empty(self):
        return len(self._data) == 0

    def push(self, e):
        self._data.append(e)

    def top(self):
        if self.is_empty():
            raise Empty('Stack is empty')
        return self._data[-1]

    def pop(self):
        if self.is_empty():
            raise Empty('Stack is empty')
        return self._data.pop(-1)

    def __repr__(self):
        return str(self._data)


def infix_to_postfix(string):
    '''
    @string: input infix expression string

    The Algorithm is described in the assignment instruction.

    @return: corresponding postfix expression string, 
             the string can include spaces, but spaces does not affect testing.
             For example, 3 2 + 4 / 3 2 * 4 + + and 32+4/32*4++ are both accepted.
    '''
    stack = ArrayStack()
    tokens = string.split(" ")
    precedence = {"+":1, "-":1, "*":2, "/":2, "(":0, ")":0}
    # To do
    
    nani = ''
    
    for i in range(len(tokens)):
        if tokens[i].isdigit() or tokens[i].isalpha():
            nani += tokens[i]
        elif tokens[i] == '(':
            stack.push(tokens[i])
        elif tokens[i] == ')':
            while stack.top() != '(':
                nani += stack.pop()
            stack.pop()
        elif tokens[i] in ['+','-','*','/']:
            if stack.is_empty():
                stack.push(tokens[i])
            else:
                while not stack.is_empty() and precedence[stack.top()] >= precedence[tokens[i]]:
                    nani += stack.pop()
                stack.push(tokens[i])
    while not stack.is_empty():
        nani += stack.pop()
    return nani


##############TEST CODES#################
''' Comment out the test code if you are grading on gradescope.'''
#print(infix_to_postfix("( 3 + 2 ) / 4 + ( 3 * 2 + 4 )")) # OUTPUTS: 3 2 + 4 / 3 2 * 4 + + 
#print(infix_to_postfix("X + Y / ( 5 * Z ) + 10"))  # OUTPUTS: X Y 5 Z * / + 10 + 
                        
                                        
