# Your task is to create functionisDivideBy (or is_divide_by) to check if an integer number is divisible by each out of two arguments.
# For example:
# is_divide_by(45, 5, 15) => True 
# is_divide_by(45, 6, 15) => False
def is_divide_by(n, a, b):
    return n%a==0 and n%b==0
