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

# ---------------------------------------------------------
# PROBLEM 3: Set .intersection() Operation
# ---------------------------------------------------------

eng_subs = int(input())

eng_set = set(map(int, input().split()))

print(eng_set)
print(type(eng_set))

fr_subs = int(input())

fr_set = set(map(int,input().split()))

print(fr_set)
print(type(fr_set))

print(len(eng_set.intersection(fr_set)))

# ---------------------------------------------------------
# PROBLEM 4: Set .union() Operation
# ---------------------------------------------------------
eng_subs = int(input())

eng_set = set(map(int,input().split()))

fr_subs = int(input())

fr_set = set(map(int,input().split()))

print(len(eng_set.union(fr_set)))

# ---------------------------------------------------------
# PROBLEM 5: Mod Divmod
# ---------------------------------------------------------
def div_operations(a, b):
    return a // b, a % b, divmod(a, b)

def main():
    a = int(input())
    b = int(input())

    quotient, remainder, div_result = div_operations(a, b)

    print(quotient)
    print(remainder)
    print(div_result)


main()

