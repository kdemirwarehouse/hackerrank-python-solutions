"""
HackerRank Python Solutions - Day 21
Date: 2025-05-04
"""

# ---------------------------------------------------------
# PROBLEM 1: Triangle Quest
# ---------------------------------------------------------
for i in range(1, int(input())):
    print(i * (10**i - 1) // 9)