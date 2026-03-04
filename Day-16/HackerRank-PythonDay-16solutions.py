"""
HackerRank Python Solutions - Day 16
Date: 2026-02-26
Author: Kadir Demir
"""

# ---------------------------------------------------------
# PROBLEM 1: Transpose and Flatten
# ---------------------------------------------------------
import numpy as np

N, M = map(int, input().split())

list1 = []

for i in range(N):
    a = list(map(int, input().split()))
    list1.append(a)

arr = np.array(list1)
print(np.transpose(arr))
print(arr.flatten())

# ---------------------------------------------------------
# PROBLEM 2: Concatenate
# ---------------------------------------------------------
import numpy as np

N, M, P = map(int, input().split())

list1 = []
list2 = []

for i in range(N):
    a = list(map(int, input().split()))
    list1.append(a)

for i in range(M):
    b = list(map(int, input().split()))
    list2.append(b)

arr1 = np.array(list1)
arr2 = np.array(list2)

print(np.concatenate((arr1, arr2), axis=0))

# ---------------------------------------------------------
# PROBLEM 3: Zeros and Ones
# ---------------------------------------------------------
import numpy as np

a = list(map(int,input().split()))

b = np.zeros(((a)), dtype=int)

print(b)

c = np.ones(((a)),dtype=int)

print(c)

# ---------------------------------------------------------
# PROBLEM 4: Eye and Identity
# ---------------------------------------------------------
import numpy as np
np.set_printoptions(legacy='1.13')

N, M = map(int, input().split())

print(np.eye(N, M))

# ---------------------------------------------------------
# PROBLEM 5: Array Mathematics
# ---------------------------------------------------------
import numpy as np 

N, M = map(int, input().split())

A = np.array([input().split() for _ in range(N)], int)

B = np.array([input().split() for _ in range(N)], int)

print(A + B)

print(A - B)

print(A * B)

print(A // B)

print(A % B)

print(A ** B)
