# ATM machines allow 4 or 6 digit PIN codes and PIN codes cannot contain anything but exactly 4 digits or exactly 6 digits. 
# If the function is passed a valid PIN string, return True, else return False..
# Example:
# validate_pin("1234") == True
# validate_pin("12345") == False
# validate_pin("a234") == False

def is_pin(pin):
    return if len(pin) in (4,6) and pin.isdigit() else False
