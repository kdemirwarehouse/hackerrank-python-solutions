"""
HackerRank Python Solutions - Day 7
Date: 2025-01-31
"""

# ---------------------------------------------------------
# PROBLEM 1: Symmetric difference
# ---------------------------------------------------------
M = int(input())
a = set(map(int,input().split()))

N = int(input())
b = set(map(int,input().split()))

result = a.symmetric_difference(b)

for i in sorted(result):
    print(i)

# ---------------------------------------------------------
# PROBLEM 2: itertools.combinations()
# ---------------------------------------------------------
from itertools import combinations

def all_combinations(s,k):
    s_sorted = sorted(s)

    for r in range(1, int(k+1)):
        combos = list(combinations(s_sorted, r))

        for combo in combos:
            print("".join(combo))




user_input = input().split()
s=user_input[0]
k=user_input[1]
all_combinations(s,k)


# ---------------------------------------------------------
# PROBLEM 3: Incorrect Regex
# ---------------------------------------------------------
import re

n = int(input())

invalid = ["**","??","++"]

for _ in range(n):
    pattern = input()

    if pattern == ".*+":
        print("False")
        continue

    if any(x in pattern for x in invalid):
        print("False")
        continue

    try:
        re.compile(pattern)
        print("True")
    except Exception:
        print("False")
# ---------------------------------------------------------
# PROBLEM 4: Set.add()
# ---------------------------------------------------------
N = int(input())

countries = set()

for _ in range(N):
    countries.add(input())

print(len(countries))

# ---------------------------------------------------------
# PROBLEM 5: itertools.combinations_with_replacement()
# ---------------------------------------------------------
from itertools import combinations_with_replacement

def all_combinations(s, k):
    s_sorted = sorted(s)

    res = combinations_with_replacement(s_sorted, int(k)) #("A","A"), ("A","C")

    for i in res:
        print("".join(i))


user_input = input().split()
s = user_input[0]
k = user_input[1]
all_combinations(s,k)



