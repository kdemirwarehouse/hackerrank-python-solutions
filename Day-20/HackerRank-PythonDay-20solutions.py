"""
HackerRank Python Solutions - Day 20
Date: 2026-03-30
Author: Kadir Demir
"""
# ---------------------------------------------------------
# PROBLEM 1: Company Logo
# ---------------------------------------------------------
from collections import Counter

def company_logo(s):
    counts = Counter(s)
    sorted_counts = sorted(counts.items(), key=lambda x: (-x[1], x[0]))
    
    for char, count in sorted_counts[:3]:
        print(char, count)


if __name__ == '__main__':
    s = input()
    company_logo(s)

