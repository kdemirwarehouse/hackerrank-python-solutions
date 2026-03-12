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




