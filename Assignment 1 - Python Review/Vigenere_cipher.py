def vigenere_encrypt(plain, key):
    '''
    @plain: a python input string. The plain text.
    @key: a python input string. The key.

    @return: the cipher python string text.
    '''
    keyLength = len(key)
    
    keyInt = [ord(i) for i in key]
    plainInt = [ord(i) for i in plain]
    
    ciphered = ''
    
    for i in range(len(plainInt)):
        value = (plainInt[i] + keyInt[i % keyLength]) % 26
        ciphered = ciphered + chr(value + 65)
        
    return ciphered

def vigenere_decrypt(cipher, key):
    '''
    @cipher: a python input string. The cipher text.
    @key: a python input string. The key.

    @return: the plain python string text.
    '''
    keyLength = len(key)
    
    keyInt = [ord(i) for i in key]
    cipherInt = [ord(i) for i in cipher]
    
    plained = ''
    
    for i in range(len(cipherInt)):
        value = (cipherInt[i] - keyInt[i % keyLength]) % 26
        plained += chr(value + 65)
    return plained
    


'''
Another note: 
To get autograded on gradescope, you program can't print anything.

Thus, please comment out the main function call, if you are submitting for auto grading.

'''
def main():
    print(vigenere_encrypt("ATTACKATDAWN", "NYUSH"))   # NRNSJXYNVHJL

    print(vigenere_encrypt("DATASTRUCTURE", "NYUSH"))   # QYNSZGPOUAHPY

    print(vigenere_encrypt("ABCDEFGHIJKLMNOPQRSTUVWXYZ", "NYUSH"))  # NZWVLSEBAQXJGFVCOLKAHTQPFM

    print(vigenere_encrypt("CUTE", "NYUSH"))  # PSNW

    print(vigenere_decrypt("NRNSJXYNVHJL", "NYUSH"))   # ATTACKATDAWN
    print(vigenere_decrypt("QYNSZGPOUAHPY", "NYUSH"))   # DATASTRUCTURE
    print(vigenere_decrypt("NZWVLSEBAQXJGFVCOLKAHTQPFM", "NYUSH"))   # ABCDEFGHIJKLMNOPQRSTUVWXYZ
    print(vigenere_decrypt("PSNW", "NYUSH"))  # CUTE

#main()