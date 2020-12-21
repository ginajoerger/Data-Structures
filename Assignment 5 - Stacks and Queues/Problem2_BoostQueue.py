from queue import Full
from queue import Empty
class BoostQueue():
    
    DEFAULT_CAPACITY = 5          # moderate capacity for all new queues

    def __init__(self):
        self._data = [None] * BoostQueue.DEFAULT_CAPACITY
        self._size = 0
        self._front = 0

    def boost(self, k): # O(k)
        '''
        @k: number of steps to boost. k is greater than zero.
        # moves the element from the back of the queue k steps forward.
        # If the queue is empty an exception is raised.
        # If k is too big (greater or equal to the number of elements in the queue) the last element will become the first.
        @return: Nothing to return
        '''
        if self._size == 0:
            raise Empty('Empty')
        elif k >= self._size:
            new = self._data[self._size - 1]
            for i in range(self._size - 1, -1, -1):
                self._data[i] = self._data[i - 1]
            self._data[0] = new
        else:
            new = self._data[self._size - 1]
            for i in range(self._size - 1, self._size - k - 1, -1):
                self._data[i] = self._data[i - 1]
            self._data[self._size - k - 1] = new

    def enqueue(self, e):
        if (self.is_full()):
            raise Full()
        self._data[(self._front + self._size) % len(self._data)] = e
        self._size += 1

    def dequeue(self):
        if self.is_empty():
            raise Empty()
        to_return = self._data[self._front]
        self._data[self._front] = None
        self._front = (self._front + 1 ) % len(self._data)
        self._size -= 1
        return to_return

    def first(self):
        if (self.is_empty()):
            raise Empty()
        return self._data[self._front]

    def is_empty(self):
        return self._size == 0

    def is_full(self):
        return (self._size == len(self._data))

    def __str__(self):
        return str(self._data)


##############TEST CODES#################
''' Comment out the test code if you are grading on gradescope.'''

#def main():
    #queue = BoostQueue()
    #queue.enqueue('a')
    #queue.enqueue('b')
    #queue.enqueue('c')
    #queue.enqueue('d')
    #queue.enqueue('e')
    #print(queue)    # a b c d e
    #queue.boost(3)  # boost e by 3
    #print(queue)    # a e b c d

#main()





