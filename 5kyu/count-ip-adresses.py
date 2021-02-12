# Implement a function that receives two IPv4 addresses, and returns the number of addresses between them 
# (including the first one, excluding the last one).
# All inputs will be valid IPv4 addresses in the form of strings. The last address will always be greater than the first one.

def toint(ip):
    out = list(map(int, ip.split('.')))
    return (16777216 * out[0]) + (65536 * out[1]) + (256 * out[2]) + out[3]

def ips_between(s, e):
    return abs(toint(s) - toint(e))
