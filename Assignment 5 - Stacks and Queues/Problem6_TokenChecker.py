# Use this stack to perform token checking. No need to modify the stack class.
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

def check_tokens(filename):
    '''
    @filename: the filename string

    Use a stack!

    @return: True if all "(""[""{""}""]"")" are matching.
             False otherwise.
    '''
    # To do
    lefty = []
    righty = []
    maybe = []
    origin = dict('() [] {}'.split())
    
    read = open(filename, "r")
    
    for i in read:
        if i == "[" or i == "{" or i == "(":
            lefty.append(i)
        elif i == "]" or i == "}" or i == ")":
            righty.append(i)
    if len(lefty) != len(righty):
        return False
    else:
        final = lefty + righty
        for x in final:
            if x in origin:
                maybe.append(x)
            elif not maybe or x != origin[maybe.pop()]:
                return False
        return not maybe


##############TEST CODES#################
''' Comment out the test code if you are grading on gradescope.'''

#def main():
    #filename = "test.c"
    #print(check_tokens(filename))  ### True

    # You can modify the test.c file to create your own test cases.

#main()



