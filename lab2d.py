#!/usr/bin/env python3

import sys


# Check for exactly 2 arguments (excluding the script name)

if len(sys.argv) != 3:

    print(f'Usage: {sys.argv[0]} name age')

    sys.exit()


# Assign arguments to variables

name = sys.argv[1]

age = sys.argv[2]


# Display the ouput

print(f'Hi {name}, you are {age} years old.')
