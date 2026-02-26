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

