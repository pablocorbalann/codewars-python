# Usually when you buy something, you're asked whether your credit card number, phone number or answer to your most secret question is still correct. However, since someone could look over your shoulder, you don't want that shown on your screen. Instead, we mask it.
# Your task is to write a function "maskify", wich changes all but the last four characters into "#"

# Examples
# maskify('891469264363') => '########4363'
# maskify('  1469264363') => '  ######4363'
# maskify('       64363') => '      ##4363'

def maskify(st):
    l = len(st)
    return st if l <= 4 else '#'*(l-4)+st[-4:]
