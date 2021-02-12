# Define a function that takes in two non-negative integers a and b and returns the last decimal digit of a^b. 
# Note that a and b may be very large!
# For example, the last decimal digit of 9^7 is 9, since 9^7=4782969. 
# The last decimal digit of (2^200)^2300, which has over 10^92 decimal digits, is 6. 
# Also, please take 0^0 = 1
#
# You may assume that the input will always be valid.
# Examples
#
#   last_digit(4, 1)                # returns 4
#   last_digit(4, 2)                # returns 6
#   last_digit(9, 7)                # returns 9
#   last_digit(10, 10 ** 10)        # returns 0
#   last_digit(2 ** 200, 2 ** 300)  # returns 6
def last_digit(a, b):
  return pow(a, b, 10)
