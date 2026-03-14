"""
HackerRank Python Solutions - Day 18
Date: 2025-03-12
Author: Kadir Demir
"""

# ---------------------------------------------------------
# PROBLEM 1: Polynomials
# ---------------------------------------------------------
import numpy as np

P = list(map(float,input().split()))

arr_p = np.array(P)

x = int(input())

print(np.polyval(arr_p, x))

# ---------------------------------------------------------
# PROBLEM 2: Linear Algebra
# ---------------------------------------------------------
import numpy as np

N = int(input())

my_list = []

for _ in range(N):
    my_list.append(list(map(float, input().split())))

A = np.array(my_list)

print(np.linalg.det(A))

# ---------------------------------------------------------
# PROBLEM 3: Write a function
# ---------------------------------------------------------
def is_leap(year):
    if year % 4 == 0 and year % 100 != 0:
        leap = True

    elif year % 400 == 0:
        leap = True

    else:
        leap = False

    return leap


year = int(input())
print(is_leap(year))




