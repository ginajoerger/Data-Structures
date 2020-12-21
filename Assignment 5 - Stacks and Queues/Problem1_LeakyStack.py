class LeakyStack():

    def __init__(self, max_size):
        self._data = [None] * max_size   # Static size
        self._size = 0    # Track current number of elements
        self._top = 0  # Use this variable to make the stack circular

    def push(self, e):  # O(1)
        if self._size < len(self._data):
            self._data[(self._top + self._size) % len(self._data)] = e
            self._size += 1
        else:
            self._data[(self._top + self._size) % len(self._data)] = e
            self._top += 1

    def pop(self):      # O(1)
        location = (self._top + self._size) % len(self._data)
        location -= 1
        new = self._data[location]
        self._data[location] = None
        self._size -= 1
        return new

    def __len__(self):  # O(1)
        return self._size

    def is_empty(self): # O(1)
        return self._size == 0

    def __str__(self):  # O(n) or O(1) up to you, not graded
        return str(self._data)

##############TEST CODES#################
''' Comment out the test code if you are grading on gradescope.'''
#def main():
    #leakystack = LeakyStack(5)  # Max size = 5 stack.
    #leakystack.push('a')
    #leakystack.push('b')
    #leakystack.push('c')
    #print(leakystack)   # top of stack --> c b a
    #leakystack.push('d')
    #leakystack.push('e')
    #print(leakystack)  # top of stack --> e d c b a 
    #leakystack.push('f')
    #print(leakystack)   # top of stack --> f e d c b,   a is gone because it is the oldest.
    #print(leakystack.pop())  # f popped
    #print(leakystack.pop())  # e popped
    #print(leakystack)   # top of stack --> d c b

#main()