#!/usr/bin/env python3

# Author: Karen Bay

# Author ID: kbay@myseneca

# Date Created: 2025/05/19


import sys


# Use command-line argument as starting value for timer

timer = int(sys.argv[1])



while timer != 0:

    print(timer)

    timer = timer - 1


print("blast off!")
