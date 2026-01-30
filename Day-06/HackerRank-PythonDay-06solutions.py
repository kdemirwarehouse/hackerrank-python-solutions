"""
HackerRank Python Solutions - Day 6
Date: 2025-01-30
"""

# ---------------------------------------------------------
# PROBLEM 1: DefaultDict Tutorial
# ---------------------------------------------------------

from collections import defaultdict

d = defaultdict(list)
n,m = map(int,input().split())


for i in range(n): #kelimeleri ve indeksleri kaydetme
    d[input()].append(str(i+1))

for j in range(m):
    print(" ".join(d[input()]) or -1)

# ---------------------------------------------------------
# PROBLEM 2: Date and Time
# ---------------------------------------------------------
import calendar

date = input()

month, day, year = map(int, date.split(" "))

days = [
    "MONDAY", "TUESDAY", "WEDNESDAY",
    "THURSDAY", "FRIDAY", "SATURDAY",
    "SUNDAY"
]

print(days[calendar.weekday(year, month, day)])
# ---------------------------------------------------------
# PROBLEM 3: Exceptions
# ---------------------------------------------------------

T = int(input())

for _ in range(T):
    try:
        a, b = map(int, input().split())
        print(a // b)
    except ZeroDivisionError as e:
        print("Error Code:",e)
    except ValueError as e:
        print("Error Code:",e)


# ---------------------------------------------------------
# PROBLEM 4: Collections.namedtuple()
# ---------------------------------------------------------
from collections import namedtuple

N = int(input())
headers = input().split()

Student = namedtuple("Student", headers)

total = 0

for _ in range(N):
    student = Student(*input().split())
    total += int(student.MARKS)

print(total / N)

# ---------------------------------------------------------
# PROBLEM 5: Collections.orderedDict()
# ---------------------------------------------------------

from collections import OrderedDict

N = int(input())
d = OrderedDict()

for i in range(N):
    line = input()
    parts = line.split()

    price = parts[-1]
    item_name = " ".join(parts[:-1])

    if item_name in d:
        d[item_name] += int(price)
    else:
        d[item_name] = int(price)

for item_name, price in d.items():
    print(f"{item_name} {price}")


