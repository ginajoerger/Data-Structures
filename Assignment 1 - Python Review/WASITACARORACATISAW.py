def palindrome(string):
    '''
    @string: the python string.

    @return: True if the input string is a palindrome.
             False otherwise.
    '''
    
    newList = list(string)
    newList2 = []
    
    for x in range(len(string)):
        y = len(string) - x - 1
        newList2.append(newList[y])
    z = ''.join(newList2)
    if z == string:
        return True
    else:
        return False


'''
Another note: 
To get autograded on gradescope, you program can't print anything.

Thus, please comment out the main function call, if you are submitting for auto grading.

'''
def main():
    print(palindrome("WASITACARORACATISAW"))

#main()