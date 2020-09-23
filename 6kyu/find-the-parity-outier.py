# You are given an array (which will have a length of at least 3, but could be very large) containing integers. The array is either entirely comprised of odd integers or entirely comprised of even integers except for a single integer N. Write a method that takes the array as an argument and returns this "outlier" N.

# Examples
# find_outlier([2, 4, 6, 7]) => 7
# find_outlier([3, 7, 11, 2]) => 2
def find_outlier(integers):
    l = list(filter(lambda x: x%2==0, integers))
    return list(filter(lambda x: x%2, integers))[0] if len(l) > 1 else l[0]
