def unique(s):
    '''
    @s: list of values.

    @return: True if all values within s are unique.
             False otherwise.
    '''
    if len(s) <= 1:
        return True
    else:
        current = s[0]
        everything_else = s[1:]
        yes = current not in everything_else
        tryAgain = unique(everything_else)
        return yes and tryAgain
        

def main():
    print(unique([1,7,6,5,4,3,1]))   # False
    print(unique([9,4,3,2,1,8]))     # True

#main()

