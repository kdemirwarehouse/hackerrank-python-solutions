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

