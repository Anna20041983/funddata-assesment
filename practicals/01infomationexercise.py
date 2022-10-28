# This is my first information exercise 
# To generate a 1000 character long string with weights based on the previous two characters

import random

# A lit of all letters 
list = 'abcdefghijklmnopqrstuvwxyz'

# Length of string
N = 1000

# Generate N random characters from list
gener = random.choices(list, k=N)

# Join them together in a string
gener = ''.join(gener)

# Create the weights based on the previous two characters
weights = [gener[::2] in list]

# Print
print(gener)