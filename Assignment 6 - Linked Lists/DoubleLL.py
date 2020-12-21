class DoubleLinkedList:

    class _Node:
        """Lightweight, nonpublic class for storing a doubly linked node."""
        __slots__ = '_element', '_next', '_prev'         # streamline memory usage

        def __init__(self, element, prev, next):      # initialize node's fields
            self._element = element               # reference to user's element
            self._prev = prev                     # reference to prev node
            self._next = next                     # reference to next node


    def __init__(self):
        """Create an empty linkedlist."""
        self._head = None
        self._tail = None
        self._size = 0


    def __len__(self):
        """Return the number of elements in the list."""
        return self._size

    def is_empty(self):
        """Return True if the list is empty."""
        return self._size == 0

    def first(self):
        """Return (but do not remove) the element at the front of the list.
        Raise Empty exception if the list is empty.
        """
        if self.is_empty():
            raise Empty('list is empty')
        return self._head._element              # front aligned with head of list

    def last(self):
        """Return (but do not remove) the element at the end of the list.

        Raise Empty exception if the list is empty.
        """
        if self.is_empty():
            raise Empty('list is empty')
        return self._tail._element


    def delete_first(self):
        """Remove and return the first element of the list.

        Raise Empty exception if the list is empty.
        """
        if self.is_empty():
            raise Empty('list is empty')
        answer = self._head._element
        self._head = self._head._next
        self._size -= 1
        if self.is_empty():                     # special case as deque is empty
            self._tail = None                     # removed head had been the tail
        else:
            self._head._prev = None
        return answer

    def delete_last(self):
        """Remove and return the last element of the list.

        Raise Empty exception if the list is empty.
        """
        if self.is_empty():
            raise Empty('list is empty')
        answer = self._tail._element
        self._tail = self._tail._prev
        self._size -= 1
        if self.is_empty():                     # special case as deque is empty
            self._head = None                     # removed tail had been the head
        else:
            self._tail._next = None
        return answer


    def add_first(self, e):
        """Add an element to the front of list."""
        newest = self._Node(e, None, self._head)   # node will be new head node, next point to old head
        if self.is_empty():
            self._tail = newest                   # special case: previously empty
        else:
            self._head._prev = newest
        self._head = newest
        self._size += 1


    def add_last(self, e):
        """Add an element to the back of list."""
        newest = self._Node(e, self._tail, None)            # node will be new tail node, prev point to old tail
        if self.is_empty():
            self._head = newest                   # special case: previously empty
        else:
            self._tail._next = newest
        self._tail = newest                     # update reference to tail node
        self._size += 1


    def __str__(self):
        result = []
        curNode = self._head
        while (curNode is not None):
            result.append(str(curNode._element) + " <--> ")
            curNode = curNode._next
        result.append("None")
        return "".join(result)


    def feed(self, otherlist, n):
        '''
        @otherlist: class DoubleLinkedList. Remove elements from this list. (Then, add removed elements to self list.)
        @n: number of elements to remove. (You can assume n is a valid input.)

        Remove several first elements from a list and inserts them as the first
        elements of another list in the original order.

        Example:
        self list(l1): 5 <--> 3 <--> 2 <--> 1 <--> None
        otherlist: 1 <--> 4 <--> 7 <--> 9 <--> None
        >>> l1.superFeed(otherlist, 3)
        l1 should become:
            1 <--> 4 <--> 7 <--> 5 <--> 3 <--> 2 <--> 1 <--> None
        otherlist should become:
            9 <--> None
        @return: Nothing
        '''

        # To do            
        if n == 0:
            return self, otherlist
        if n > 0:
            a = otherlist.delete_first()
            self.feed(otherlist, n - 1)
            self.add_first(a)

    def del_anything_occured(self, otherlist):
        '''
        @otherlist: class DoubleLinkedList. Use values stored within this list.

        Remove nodes from self linked list, any node that contains any value appeared in otherlist.

        Example:
        self list(l1):
        18 <--> 16 <--> 14 <--> 12 <--> 10 <--> 18 <--> 16 <--> 14 <--> 12 <--> 10 <--> None
        otherlist: 
        18 <--> 16 <--> 14 <--> 12 <--> None
        >>> l1.del_anything_occured(otherlist)
        l1 should become:
            10 <--> 10 <--> None
        otherlist should remain the same:
            18 <--> 16 <--> 14 <--> 12 <--> None
        '''
        
        if self.is_empty():
            raise Empty('list is empty') 
            
        a = otherlist._head
        
        for i in range(0, len(otherlist)):
            curr = self._head
            while (curr is not None):
                if curr._element == a._element:
                    if curr._prev == None:
                        self.delete_first()
                        curr = self._head
                    else:
                        if curr._next == None:
                            self.delete_last()
                            curr = None
                        else:
                            curr._prev._next = curr._next
                            curr._next._prev = curr._prev
                            curr = curr._next
                            self._size -= 1
                else:
                    curr = curr._next
            a = a._next


###############Comment out test code if submitting on gradescope#############
#def main():
    #print("-----------Testing feed-------------")
    #l1 = DoubleLinkedList()
    #l2 = DoubleLinkedList()
    #for i in range(5):
        #l1.add_first(i * 2)
    #for j in range(5):
        #l2.add_first(j * 3)
    #print(l1) # 8 <--> 6 <--> 4 <--> 2 <--> 0 <--> None
    #print(l2) # 12 <--> 9 <--> 6 <--> 3 <--> 0 <--> None
    #l1.feed(l2, 3)
    #print(l1, ", Expected: 12 <--> 9 <--> 6 <--> 8 <--> 6 <--> 4 <--> 2 <--> 0 <--> None") # 
    #print(l2, ", Expected: 3 <--> 0 <--> None")


    #print("-----------Testing del_anything_occured-------------")
    #l1 = DoubleLinkedList()
    #l2 = DoubleLinkedList()
    #for i in range(10):
        #l1.add_first(i * 2)
    #for j in range(10):
        #l2.add_first(j * 3)
    #print(l1)   # 18 <--> 16 <--> 14 <--> 12 <--> 10 <--> 8 <--> 6 <--> 4 <--> 2 <--> 0 <--> None
    #print(l2)   # 27 <--> 24 <--> 21 <--> 18 <--> 15 <--> 12 <--> 9 <--> 6 <--> 3 <--> 0 <--> None
    #l1.del_anything_occured(l2)
    #print(l1, ", Expected: 16 <--> 14 <--> 10 <--> 8 <--> 4 <--> 2 <--> None")
    #print(l2, ", l2 should remain the same.")

    
#main()







