# ROT13 is a simple letter substitution cipher that replaces a letter with the letter 13 letters after it in the alphabet.
# ROT13 is an example of the Caesar cipher.
# Create a function that takes a string and returns the string ciphered with Rot13. 
# If there are numbers or special characters included in the string, they should be returned as they are.
# Only letters from the latin/english alphabet should be shifted, like in the original Rot13 "implementation".

def rot13(s):
    rot=lambda x:chr(ord(x)+13) if chr(ord(x.lower())+13).isalpha()==True else chr(ord(x)-13)
    s=[rot(i) for i in filter(lambda x:x!=',',map(str,s))]
    return ''.join(s)
