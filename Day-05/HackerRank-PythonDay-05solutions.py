"""
HackerRank Python Solutions - Day 5
Date: 2025-01-28
"""

# ---------------------------------------------------------
# PROBLEM 1: itertools.product()
# ---------------------------------------------------------
from itertools import product

n, m = map(int,input().split())

a, b = map(int,input().split())

result = product(range(n,m+1),range(a,b+1))

print(*list(result))

# ---------------------------------------------------------
# PROBLEM 2: collections.Counter()
# ---------------------------------------------------------
import collections

NUMBER_OF_SHOES = int(input())
SIZES_IN_STOCK = collections.Counter(map(int,input().split()))

TOTAL_REVENUE = 0

for _ in range(int(input())):
    size, price = map(int,input().split())
    if size in SIZES_IN_STOCK:
        NUMBER_OF_SHOES -= 1
        TOTAL_REVENUE += price

print(TOTAL_REVENUE)

# ---------------------------------------------------------
# PROBLEM 3: itertools.permutations()
# ---------------------------------------------------------
import itertools

letters = []

for i in input().upper():
    if i.isalpha():
        letters.append(i)

letters = sorted(letters)

for p in itertools.permutations(letters, 2):
    concatenated = "".join(p)
    print(concatenated)


# ---------------------------------------------------------
# PROBLEM 3: itertools.permutations(), alternative
# ---------------------------------------------------------
from itertools import permutations

def per(s, size):
    return "\n".join(sorted(["".join(i) for i in permutations(s,size)]))


user = input().split(" ")

s, size = user[0], int(user[1])

print(per(s,size))

# ---------------------------------------------------------
# PROBLEM 4: Polar Coordinates
# ---------------------------------------------------------
import cmath

z = complex(input())

r = abs(z)

print(r)
print(cmath.phase(z))
# ---------------------------------------------------------
# PROBLEM 5: Introduction to Sets
# ---------------------------------------------------------
def average(array):
    '''Calculates the average of the array'''
    s = set(arr)
    return float(sum(s)) / len(s)

if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    result = average(arr)
    print(result)