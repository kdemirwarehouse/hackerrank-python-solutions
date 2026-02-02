"""
HackerRank Python Solutions - Day 8
Date: 2026-02-02
"""

# ---------------------------------------------------------
# PROBLEM 1: Set .discard(), .remove() & .pop()
# ---------------------------------------------------------
n = int(input())
s = set(map(int, input().split()))

N = int(input())

for _ in range(N):
    command = input().split()

    if command[0] == "pop":
        s.pop()
    elif command[0] == "remove":
        s.remove(int(command[1]))
    elif command[0] == "discard":
        s.discard(int(command[1]))

print(sum(s))

# ---------------------------------------------------------
# PROBLEM 2:collections.deque()
# ---------------------------------------------------------
from collections import deque

N = int(input())

d = deque()

for _ in range(N):
    command = input().split()

    if command[0] == "append":
        d.append(int(command[1]))
    elif command[0] == "pop":
        d.pop()
    elif command[0] == "popleft":
        d.popleft()
    elif command[0] == "appendleft":
        d.appendleft(int(command[1]))

print(*d)

