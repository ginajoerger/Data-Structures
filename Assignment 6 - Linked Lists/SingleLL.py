class SingleLinkedList:

    class _Node:
        """Lightweight, nonpublic class for storing a singly linked node."""
        __slots__ = '_element', '_next'         # streamline memory usage

        def __init__(self, element, next):      # initialize node's fields
            self._element = element               # reference to user's element
            self._next = next                     # reference to next node

    def __init__(self):
        """Create an empty linkedlist."""
        self._head = None
        self._size = 0

    def __len__(self):
        """Return the number of elements in the linkedlist."""
        return self._size

    def is_empty(self):
        """Return True if the linkedlist is empty."""
        return self._size == 0

    def top(self):
        """Return (but do not remove) the element at the top of the linkedlist.

        Raise Empty exception if the linkedlist is empty.
        """
        if self.is_empty():
            raise Empty('list is empty')
        return self._head._element              # head of list

    def insert_from_head(self, e):
        """Add element e to the head of the linkedlist."""
        # Create a new link node and link it
        new_node = self._Node(e, self._head)
        self._head = new_node
        self._size += 1

    def delete_from_head(self):
        """Remove and return the element from the head of the linkedlist.

        Raise Empty exception if the linkedlist is empty.
        """
        if self.is_empty():
            raise Empty('list is empty')
        to_return = self._head._element
        self._head = self._head._next
        self._size -= 1
        return to_return

    def __str__(self):
        result = []
        curNode = self._head
        while (curNode is not None):
            result.append(str(curNode._element) + "-->")
            curNode = curNode._next
        result.append("None")
        return "".join(result)


    def remove_all_occurance(self, value):
        '''
        @value: the value we are trying to remove from the self list.
        remove any node that contains value in self linked list. Return nothing.
        Example:
        l1: 5 --> 4 --> 2 --> 4 --> 1 --> 9 --> 4 --> None
        >>> l1.remove_all_occurance(4)
        l1 should become: 5 --> 2 --> 1 --> 9 --> None
        @return: Nothing
        '''
        #To Do
        temp = self._head
        while temp is not None and temp._element == value:
            self.delete_from_head()
            temp = self._head
        if self._head is not None:
            while temp._next is not None:
                if temp._next._element == value:
                    temp._next = temp._next._next
                else:
                    temp = temp._next            
               
    def sameSame(self, otherlist):
        '''
        @otherlist: the list comparing with self list.
        Checks whether two lists contain the same elements in the same order
        returns True if same, return False otherwise.

        Example:
        l1: 5 --> 4 --> 2 --> None
        l2: 5 --> 4 --> 2 --> None
        >>> l1.sameSame(l2)
        >>> True

        @return: True or False
        '''
        # To do
        a = self._head
        b = otherlist._head
        
        while (a != None and b != None):
            if (a._element != b._element):
                return False
            
            a = a._next
            b = b._next
        
        return (a == None and b == None)


    def reverse(self):
        '''
        reverses self list.
        Example:
        1 --> 2 --> 3 --> 4 --> None
        >>> l.reverse()
        4 --> 3 --> 2 --> 1 --> None
        @return: Nothing
        '''
        # To do   
        prev = None
        curr = self._head
        
        while (curr is not None):
            nex = curr._next
            curr._next = prev
            prev = curr
            curr = nex
        self._head = prev

    def sublist(self, otherlist):
        '''
        @otherlist: class SingleLinkedList. 
        Return True if otherlist is sublist of self. Return False otherwise.
        (Definition of sublist: A list that makes up part of a larger list)
        
        Example:
        self list(l1):
        1 --> 2 --> 3 --> 4 --> None
        otherlist: 
        None; 1 --> None; 1 --> 2 --> None; 1 --> 2 --> 3 --> None;
        1 --> 2 --> 3 --> 4 --> None; 2 --> None; 2 --> 3 --> None;
        2 --> 3 --> 4 --> None; 3 --> None; 3 --> 4 --> None; 4 --> None
        Are valid sublists. Should return True for any of the above cases.
        >>> l1.sublist(otherlist)
        True

        otherlist: 
        1 --> 1 --> None
        >>> l1.sublist(otherlist)
        False

        @return: True or False
        '''
        if self.is_empty():
            raise Empty('list is empty')
            
        top = len(self)
        bottom = len(otherlist)
        curr = self._head
        if bottom == 0:
            return True
        elif top >= bottom:
            for i in range(0, top):
                if curr._element == otherlist._head._element:
                    redo = SingleLinkedList()
                    moreCurr = curr
                    for i in range(0, bottom):
                        if moreCurr == None:
                            return False
                        
                        redo.insert_from_head(moreCurr._element)
                        moreCurr = moreCurr._next
                    redo.reverse()
                    if redo.sameSame(otherlist):
                        return True
                curr = curr._next
            return False
        else:
            return True
            

###############Comment out test code if submitting on gradescope#############
#def main():
    #print("-----------Testing remove_all_occurance-------------")
    #l1 = SingleLinkedList()
    #for i in range(10):
        #l1.insert_from_head(6)
    #print(l1)  # 6-->6-->6-->6-->6-->6-->6-->6-->6-->6-->None
    #l1.remove_all_occurance(6)
    #print(l1, "Expected: None")
    #print()

    #l1 = SingleLinkedList()
    #for i in range(10):
        #l1.insert_from_head(i % 2)
    #print(l1)  # 1-->0-->1-->0-->1-->0-->1-->0-->1-->0-->None
    #l1.remove_all_occurance(0)
    #print(l1, "Expected: 1-->1-->1-->1-->1-->None")
    #print()

    #print("-----------Testing sameSame-------------")
    #l1 = SingleLinkedList()
    #l2 = SingleLinkedList()
    #for i in range(5):
        #l1.insert_from_head(i)
        #l2.insert_from_head(i)
    #print("Is l1 sameSame l2? Your answer:", l1.sameSame(l2), ", Expected: True")   # True
    #print()
    
    #print("-----------Testing reverse-------------")
    #l1 = SingleLinkedList()
    #for i in range(10):
        #l1.insert_from_head(i)
    #print(l1)  # 9-->8-->7-->6-->5-->4-->3-->2-->1-->0-->None
    #l1.reverse()
    #print(l1, "Expected: 0-->1-->2-->3-->4-->5-->6-->7-->8-->9-->None")

    #print("-----------Testing sublist-------------")
    #l1 = SingleLinkedList()
    #l2 = SingleLinkedList()
    #for i in range(10):
        #l1.insert_from_head(i)
    #for i in range(5):
        #l2.insert_from_head(i + 3)
    #print(l1)
    #print(l2)
    #print("Is l2 sublist of l1? Your answer:", l1.sublist(l2), ", Expected: True")


#main()



