"""
HackerRank Python Solutions - Day 22
Date: 2025-06-02
"""

# ---------------------------------------------------------
# PROBLEM 1: Reduce Function
# ---------------------------------------------------------
from fractions import Fraction
from functools import reduce

def product(fracs):
    t = reduce (lambda x,y: x*y, fracs)
    return t.numerator, t.denominator

if __name__ == '__main__':
    fracs = []
    for _ in range(int(input())):
        fracs.append(Fraction(*map(int, input().split())))
    result = product(fracs)


# ---------------------------------------------------------
# PROBLEM 2: Regex Substitution
# ---------------------------------------------------------

N = int(input())

for i in range(N):
    line = input()
    while (" && " in line) or (" || " in line):
        line = line.replace(" && ", " and ")
        line = line.replace(" || ", " or ")
    
    print(line)

# ---------------------------------------------------------
# PROBLEM 3: Validating Credit Card Numbers
# ---------------------------------------------------------
import re


for _ in range(int(input())):
    num = input()

    ok1 = bool(re.match(r"^[456]\d{15}$", num))
    ok2 = bool(re.match(r"^[456]\d{3}\-\d{4}\-\d{4}\-\d{4}$", num))
    num = num.replace("-", "")
    ok3 = bool(re.match(r"(?!.*(\d)(-?\1){3})", num))
    if (ok1 or ok2) and ok3:
        print("Valid")
    else:
        print("Invalid")

# ---------------------------------------------------------
# PROBLEM 4: Validating Credit Card Numbers
# ---------------------------------------------------------
regex_integer_in_range = r"^[1-9][0-9]{5}$"	
regex_alternating_repetitive_digit_pair = r"(\d)(?=\d\1)"	

import re
P = input()

print (bool(re.match(regex_integer_in_range, P)) 
and len(re.findall(regex_alternating_repetitive_digit_pair, P)) < 2)

# ---------------------------------------------------------
# PROBLEM 5: Matrix Script
# ---------------------------------------------------------

import math
import os
import random
import re
import sys



first_multiple_input = input().rstrip().split()

n = int(first_multiple_input[0])

m = int(first_multiple_input[1])

matrix = []

for _ in range(n):
    matrix_item = input()
    matrix.append(matrix_item)

decoded = ""

for col in range(m):
    for row in range(n):
        decoded += matrix[row][col]
        
cleaned = re.sub(
    r"(?<=[A-Za-z0-9])[^A-Za-z0-9]+(?=[A-Za-z0-9])",
    " ",
    decoded
)

print(cleaned)
