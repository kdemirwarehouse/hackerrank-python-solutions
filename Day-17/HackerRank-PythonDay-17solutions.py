"""
HackerRank Python Solutions - Day 17
Date: 2026-03-04
"""

# ---------------------------------------------------------
# PROBLEM 1: Floor, Ceil and Rint
# ---------------------------------------------------------
import numpy as np
np.set_printoptions(legacy='1.13')

A = np.array(list(map(float ,input().split())))

print(np.floor(A))
print(np.ceil(A))
print(np.rint(A))

# ---------------------------------------------------------
# PROBLEM 2: Sum and Prod
# ---------------------------------------------------------
import numpy as np

N, M = map(int,input().split())

my_list = []

[my_list.append(list(map(int, input().split()))) for _ in range(N)]

my_array = np.array(my_list)

a = np.sum(my_array, axis = 0)

print(np.prod(a, axis=None))

# ---------------------------------------------------------
# PROBLEM 3: Min and Max
# ---------------------------------------------------------
import numpy as np 

N, M = map(int, input().split())

my_list = []

[my_list.append(list(map(int, input().split()))) for _ in range(N)]

my_array = np.array(my_list)

min_value = np.min(my_array, axis = 1)

print (np.max(min_value))

