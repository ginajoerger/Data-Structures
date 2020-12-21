def exist_pair(L, X):
    ''' Detect whether we can find two elements in L whose sum is exactly X.
    @L: a python list of integers
    @X: integer X

    Required runtime: Expected O(len(L))

    return: True if we can find two elements in L whose sum is exactly X. False otherwise.
    '''
    # To do
    new = {}
    
    for i in L:
        if X - i not in new:
            new[X - i] = 0
        if i in new:
            return True
    return False
    

def main():
    l1 = [20, 36, 35, 46, 25, 27, 8, 0, 34, 31]

    print("20 + 36 = 56, Should return True........")
    print("Your result:", exist_pair(l1, 56))
    print("36 + 34 = 70, Should return True........")
    print("Your result:", exist_pair(l1, 70))
    print("36 + 0 = 36, Should return True........")
    print("Your result:", exist_pair(l1, 36))
    print("No pair with sum equal to 74....")
    print("Your result:", exist_pair(l1, 74))

#main()


