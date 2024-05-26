import sys

# number = sys.argv[1]
number = '+7-111-222-33-44'

number = number.\
    replace('-', ' (', 1).\
    replace('-', ') ', 1)
    # replace('-')
print(number)