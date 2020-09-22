# Implement a method tht accepts 3 integer values "a, b and c". 
# The method should return True if a triangle can be built with the sides of given length and False in any other case.
# All triangles must have surface greater than 0 to be accepted

def is_triangle(a, b, c):
    return True if a+b>c and a+c>b and c+b>a else False
