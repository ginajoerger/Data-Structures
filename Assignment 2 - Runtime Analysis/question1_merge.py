def merge(I1, I2):  
    '''
    @I1: the first iterable object. Can be a string!
    @I2: the second iterable object.

    required runtime: O(n).
    @return: alternately merged I1, I2 elements in a list.
    '''      
        
    a = []
    b = []
    c = []
    
    for i in I1:
        a.append(i)
        
    for j in I2:
        b.append(j)
        
    if len(a) >= len(b):
        more = a
        less = b
        
    else:
        more = b
        less = a
        
    for k in range(0, len(more)):
        if k < len(a):
            c.append(a[k])
        if k < len(b):
            c.append(b[k])
            
    return(c)

'''
Note: 
To get autograded on gradescope, you program can't print anything.

Thus, please comment out the main function call, if you are submitting for auto grading.

'''
def main():
    print([i for i in merge("what",range(100,105))])
    print([i for i in merge(range(5),range(100,101))]) 
    print([i for i in merge(range(1),range(100,105))])

#main()