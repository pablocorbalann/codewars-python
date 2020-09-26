# Given an array of integers, find the one that appears an odd number of times.
# There will always be only one integer that appears an odd number of times.
def find_it(seq):
    return list(filter(lambda x: seq.count(x) % 2, seq))[0]