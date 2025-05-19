#!/usr/bin/env python3

# Author: Karen Bay

# Author ID: kbay@myseneca

# Date Created: 2025/05/19


import sys


# Check if an argument was entered

if len(sys.argv) > 1:

    timer = int(sys.argv[1])

else:

    timer = 3


while timer != 0:

    print(timer)

    timer = timer - 1


print("blast off!")
