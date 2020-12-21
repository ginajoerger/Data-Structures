import random

class Item():
    def __init__(self, k, v):
        self._key = k
        self._value = v

    def __eq__(self, other):               
        return self._key == other._key   # compare items based on their keys

    def __ne__(self, other):
        return not (self == other)       # opposite of __eq__

    def __lt__(self, other):               
        return self._key < other._key    # compare items based on their keys

class CuckooHashTable():
    def __init__(self):
        self._size=0
        self._maxsize = 11
        self._array1 = [None] * self._maxsize
        self._array2 = [None] * self._maxsize
        self._random1 = random.random()
        self._random2 = random.random()


    def _hash1(self, key):
        return hash((key, self._random1)) % self._maxsize

    def _hash2(self, key):
        return hash((key, self._random2)) % self._maxsize


    def __getitem__(self,key):
        ''' given key, return the value associated with key
            use hash1/hash2 to compute the index.
            raise KeyError if not found.
        '''
        first = self._array1[self._hash1(key)]
        second = self._array2[self._hash2(key)]
        
        if first is not None and first._key == key:
            return first._value
        elif second is not None and second._key == key:
            return second._value
        else:
            raise Exception("Error")
        

    def __setitem__(self,k,v): 
        ''' if key k exists in either array, modify associated value to v.
            if key k does not exist in both arrays, insert (k, v) into table as a new class Item.
            if cycles, resize (rehash) the table.
            terminate the function until we finally find a location for k.
            You may want to use the _resize function for cycle 
        '''
        first = self._hash1(k)
        second = self._hash2(k)
        
        newItem = Item(k,v)
        maxx = self._size * 2
        
        if self._array1[first] is None:
            self._array1[first] = newItem
            self._size += 1
        else:
            out = self._array1[first]
            new = 0
            
            while new <= maxx:
                first = self._hash1(newItem._key)
                second = self._hash2(newItem._key)
                
                if new % 2 == 1:
                    if self._array1[first] is None:
                        self._array1[first] = newItem
                        self._size += 1
                        break
                    else:
                        out = self._array2[second]
                        self._array2[second] = out
                        
                else:
                    if self._array2[second] is None:
                        self._array2[second] = newItem
                        self._size += 1
                        break
                    else:
                        out = self._array1[first]
                        self._array1[first] = out
                new += 1
                
            if new == maxx + 1:
                self._resize()
                self.__setitem__(k,v)
        

    def __delitem__(self,k): 
        ''' given key, set self._array1 or self._array2 corresponding index to None.
            raise KeyError if key not found.
        '''
        first = self._array1[self._hash1(k)]
        second = self._array2[self._hash2(k)]
        
        if first is not None and first._key == k:
            self._array1[self._hash1(k)] = None
            self._size -= 1
            return True
        elif second is not None and second._key == k:
            self._array2[self._hash2(k)] = None
            self._size -= 1
            return True
        else:
            raise Exception("Error")

    def _resize(self):
        ''' double the size of self._array1, self._array2.
            also self._maxsize
            Remember to rehash all the old (key, value) pairs!
        '''
        original = list(self.items())
        self._size = 0
        
        self._random1 = random.random()
        self._random2 = random.random()
                        
        self._maxsize = self._maxsize * 2
        self._array1 = [None] * ((self._maxsize * 2) - 1)
        self._array2 = [None] * ((self._maxsize * 2) - 1)
        
        for i in original:
            self.__setitem__(i._key, i._value)

    def __len__(self): 
        return self._size

    def __contains__(self,key): 
        ''' return True if key exists in table
            return False otherwise
        '''
        first = self._array1[self._hash1(key)]
        second = self._array2[self._hash2(key)]
        
        if first is not None and first._key == key:
            return True
        elif second is not None and second._key == key:
            return True
        else:
            return False

    def __iter__(self):
        ''' same as keys(self) '''
        for i in self._array1:
            if i is not None:
                yield i._key
        for j in self._array2:
            if j is not None:
                yield j._key

    def keys(self): 
        ''' yield an generator of keys in table '''
        for i in self._array1:
            if i is not None:
                yield i._key
        for j in self._array2:
            if j is not None:
                yield j._key

    def values(self): 
        ''' yield an generator of values in table '''
        for i in self._array1:
            if i is not None:
                yield i._value
        for j in self._array2:
            if j is not None:
                yield j._value

    def items(self):
        ''' yield an generator of Items in table '''
        for i in self._array1:
            if i is not None:
                yield i
        for j in self._array2:
            if j is not None:
                yield j

def main():
    table = CuckooHashTable()
    for i in range(200):        # Tests __setitem__, insert 0 ~ 199. _resize() also need to work correctly.
        table[i] = "happy_coding"
    
    print(len(table))           # Tests __len__, should be 200.

    for j in range(195):        # Tests __delitem__, delete 0 ~ 194
        del table[j]

    print(len(table))           # Tests __len__, should be 5.

    for j in table.items():     # Tests items()
        print(j._key)           # 195, 196, 197, 198, 199 left in table

    print(table[196])           # Tests __getitem__
                                # Should print "happy_coding"
    
#main()

