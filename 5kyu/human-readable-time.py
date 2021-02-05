# Write a function, which takes a non-negative integer (seconds) as input and returns the time in a human-readable format (HH:MM:SS)
#   HH = hours, padded to 2 digits, range: 00 - 99
#   M = minutes, padded to 2 digits, range: 00 - 59
#   SS = seconds, padded to 2 digits, range: 00 - 59
# The maximum time never exceeds 359999 (99:59:59)

def make_readable(seconds):
    minutes = seconds // 60
    hours = minutes // 60
    return '{2}:{1}:{0}'.format(str(seconds - minutes * 60).zfill(2),
                                str(minutes - hours * 60).zfill(2),
                                str(hours).zfill(2))
