class SharedMemoryStack():
    '''
    Design two stacks that share the same Python list, self._data.
    Both stacks can grow independently;

    no new item can be pushed in either stack when self._data is full.
    '''

    DEFAULT_CAPACITY = 10

    def __init__(self):
        self._data = [None] * SharedMemoryStack.DEFAULT_CAPACITY
        self.stack1_size = 0
        self.stack2_size = 0

    def pushStack1(self, e):
        self._data[self.stack1_size] = e
        self.stack1_size += 1

    def pushStack2(self, e):
        self._data[-self.stack2_size - 1] = e
        self.stack2_size += 1

    def popStack1(self):
        new = self._data[self.stack1_size - 1]
        self._data[self.stack1_size - 1] = None
        self.stack1_size -= 1
        return new

    def popStack2(self):
        new = self._data[-((self.stack2_size) % SharedMemoryStack.DEFAULT_CAPACITY)]
        self._data[-((self.stack2_size) % SharedMemoryStack.DEFAULT_CAPACITY)] = None
        self.stack2_size -= 1
        return new

    def is_full(self):
        return self.stack1_size + self.stack2_size == SharedMemoryStack.DEFAULT_CAPACITY

    def is_empty1(self):
        return self.stack1_size == 0

    def is_empty2(self):
        return self.stack2_size == 0

    def peekStack1(self):
        return self._data[self.stack1_size - 1]

    def peekStack2(self):
        return self._data[len(self._data) - self.stack2_size]

    def __str__(self):   # Not graded.
        result = []
        result.append("Stack 1: ")
        # Your code 1 to show stack 1
        if not self.is_empty1():
            for i in range(0, self.stack1_size):
                result += str(self._data[i]) + ',' + ' '
            result.pop(-1)
            result[-1] = ' '
        
        result.append("Stack 2: ")
        # Your code 2 to show stack 2
        if not self.is_empty2():
            for x in range(len(self._data) - 1, (len(self._data) - self.stack2_size - 1), -1):
                result += str(self._data[x]) + ',' + ' '
            result.pop(-1)
            result[-1] = ' '

        return "".join(result)


##############TEST CODES#################
''' Comment out the test code if you are grading on gradescope.'''

#def main():
    #stack = SharedMemoryStack()
    #stack.pushStack1(1)
    #stack.pushStack1(2)
    #stack.pushStack1(3)
    #stack.pushStack1(4)
    #stack.pushStack2(5)
    #stack.pushStack2(6)
    #stack.pushStack2(7)
    #stack.pushStack2(8)
    #stack.pushStack2(9)
    ##print(stack)  # Stack 1: 1, 2, 3, 4; Stack 2: 5, 6, 7, 8, 9, 10
    #print("Popping: ", stack.popStack1())  # popped 4
    #stack.pushStack2(11) # Stack 1: 1, 2, 3; Stack 2: 5, 6, 7, 8, 9, 10, 11
    #print(stack)

#main()






