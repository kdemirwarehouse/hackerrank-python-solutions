"""
HackerRank Python Solutions - Day 8
Date: 2026-02-07
"""

# ---------------------------------------------------------
# PROBLEM 1: Detect Floating Point Number
# ---------------------------------------------------------

import re
N = int(input())

for _ in range(N):
    print(True if re.match(r"[+-]?[0-9]*\.[0-9]+$", input()) else False)


# ---------------------------------------------------------
# PROBLEM 2: Map and Lambda Function
# ---------------------------------------------------------

cube = lambda x : x ** 3

def fibonacci(n):
    fib_list = []
    for i in range(n):
        fib_list.append(i if i == 0 or i == 1 else fib_list[i - 1] + fib_list[i - 2])
    return fib_list

if __name__ == '__main__':
    n = int(input())
    print(list(map(cube, fibonacci(n))))

# ---------------------------------------------------------
# PROBLEM 3: Re.split()
# ---------------------------------------------------------
regex_pattern = r"[,.]"

import re
print("\n".join(re.split(regex_pattern, input())))

# ---------------------------------------------------------
# PROBLEM 4: Group(), Groups() & Groupdict()
# ---------------------------------------------------------
import re

S = input()

fount_it = re.search(r"([a-zA-Z0-9])\1+",S)

if re.search:
    print(fount_it.group(1))
else:
    print(-1)

# ---------------------------------------------------------
# PROBLEM 5: Re.start() & Re.end()
# ---------------------------------------------------------
import re

string = input()
substring = input()

pattern = re.compile(substring)
match = pattern.search(string)
if not match: print('(-1, -1)')
while match:
    print('({0}, {1})'.format(match.start(), match.end() - 1))
    match = pattern.search(string, match.start() + 1)

