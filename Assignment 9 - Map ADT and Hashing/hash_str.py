def hash_str(string):
    ''' return a integer hash value for the given string.
        you should follow the hash function property:
        1. hash same thing gives the same result.
        2. hash different thing should give different result. The more different, the better.

        @string: the string to be hashed.

        return: integer value, the hash value for given string.

        Hint: Be creative! There are many correct answers.
    '''
    # To do
    
    h = 150
    for i in string:
        h = (( h << 7) + h) + ord(i)
    return h

''' This question can not get autograded. '''
def main():
    print("Hash lee: ", hash_str("lee"))
    print("Hash Lee: ", hash_str("Lee"))
    print("Hash ele: ", hash_str("ele"))
    print("Hash eel: ", hash_str("eel"))
    for i in range(5):
        print("Hash lee: ", hash_str("lee"))

main()