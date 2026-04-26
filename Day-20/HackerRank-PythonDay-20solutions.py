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

# ---------------------------------------------------------
# PROBLEM 2: Piling Up!
# ---------------------------------------------------------
t = int(input())

for _ in range(t):
    n = int(input())
    blocks = list(map(int, input().split()))

    left = 0
    right = n - 1
    last = float('inf')  

    possible = True

    while left <= right:
        if blocks[left] >= blocks[right]:
            pick = blocks[left]
            left += 1
        else:
            pick = blocks[right]
            right -= 1

        if pick > last:
            possible = False
            break

        last = pick

    print("Yes" if possible else "No")

# ---------------------------------------------------------
# PROBLEM 3: Triangle Quest 2
# ---------------------------------------------------------
for i in range(1, int(input()) + 1):
    print(((10 ** i - 1) // 9) ** 2)



