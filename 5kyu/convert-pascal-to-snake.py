
# Complete the function/method so that it takes CamelCase string and returns the string in snake_case notation. 
# Lowercase characters can be numbers. If method gets number, it should return string.
def to_underscore(string):
    s = ''
    for i, letter in enumerate(str(string)):
        if letter != letter.lower():
            s += '{0}{1}'.format('_' if i!=0 else '', letter.lower())
        else:
            s += letter
    return s
