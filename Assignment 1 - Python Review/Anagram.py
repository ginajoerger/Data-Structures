def anagram(string1, string2):
    '''
    @string1: the first python string.
    @string2: the second python string.

    @return: True if string1 is anagram of string2
             False otherwise.
    '''
    #Take both strings del punctuation, space
    #put both strings into individual lists
    #loop through string1 and make dictionary

    newDict1 = {}
    newDict2 = {}
    
    newList1 = list(string1)
    while ' ' in newList1:
        newList1.remove(' ')
        
    newList2 = list(string2)
    while ' ' in newList2:
        newList2.remove(' ')
        
    for x in newList1:
        newDict1[x] = newList1.count(x)
    for y in newList2:
        newDict2[y] = newList2.count(y)
        
    for z in newDict1.keys():
        if not z in newDict2.keys() or newDict1[z] != newDict2[z]:
            return False
    return True
    

'''
Another note: 
To get autograded on gradescope, you program can't print anything.

Thus, please comment out the main function call, if you are submitting for auto grading.

'''

def main():
    string1 = "william shakespeare"
    string2 = "i am a weakish speller"
    print(anagram(string1, string2))   

    string1 = "software"
    string2 = "swear oft"
    print(anagram(string1, string2))  

#main()