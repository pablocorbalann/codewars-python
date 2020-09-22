# Create a function that takes an integer as input and returns the number of bits that are equal to one in the binary representation of that number. 
# You can guarantee that input is non-negative.

# Example 
# count_bits(1234) => 10011010010 => 5

def count_bits(num):
    return len(tuple(filter(lambda x: x=='1', f'{n:b}')))
