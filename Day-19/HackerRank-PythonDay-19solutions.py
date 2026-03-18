"""
HackerRank Python Solutions - Day 19
Date: 2026-03-17
"""

# ---------------------------------------------------------
# PROBLEM 1: Time Delta
# ---------------------------------------------------------
import os
from datetime import datetime

def time_delta(t1, t2):
    fmt = "%a %d %b %Y %H:%M:%S %z"
    dt1 = datetime.strptime(t1, fmt)
    dt2 = datetime.strptime(t2, fmt)
    delta_seconds = abs(int((dt1 - dt2).total_seconds()))
    return str(delta_seconds)



if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input())

    for t_itr in range(t):
        t1 = input()

        t2 = input()

        delta = time_delta(t1, t2)

        fptr.write(delta + '\n')

    fptr.close()

# ---------------------------------------------------------
# PROBLEM 2: Find Angle MBC
# ---------------------------------------------------------
import math

AB = int(input())

BC = int(input())

angle = math.atan(AB/BC)

angle = math.degrees(angle)

alfa = round(angle)

print(str(alfa) + "\u00b0")


