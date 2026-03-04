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

