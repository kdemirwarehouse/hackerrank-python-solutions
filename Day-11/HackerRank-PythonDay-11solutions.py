"""
HackerRank Python Solutions - Day 2
Date: 2025-02-06
"""
# ---------------------------------------------------------
# PROBLEM 1: Class 2 - Find the Torsional Angle
# ---------------------------------------------------------
import math


class Points(object):
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    def __sub__(self, no):
        return Points(
            self.x - no.x,
            self.y - no.y,
            self.z - no.z
        )

    def dot(self, no):
        return self.x * no.x + self.y * no.y + self.z * no.z

    def cross(self, no):
        x = self.y * no.z - self.z * no.y
        y = self.z * no.x - self.x * no.z
        z = self.x * no.y - self.y * no.x
        return Points(x, y, z)

    def absolute(self):
        return pow((self.x ** 2 + self.y ** 2 + self.z ** 2), 0.5)


if __name__ == '__main__':
    points = list()
    for i in range(4):
        a = list(map(float, input().split()))
        points.append(a)

    a, b, c, d = Points(*points[0]), Points(*points[1]), Points(*points[2]), Points(*points[3])
    x = (b - a).cross(c - b)
    y = (c - b).cross(d - c)
    angle = math.acos(x.dot(y) / (x.absolute() * y.absolute()))

    print("%.2f" % math.degrees(angle))


# ---------------------------------------------------------
# PROBLEM 2: Input()
# ---------------------------------------------------------
x, k = map(int, input().split())
print(eval(input()) == k)
#---------------------------------------------------------
# PROBLEM 3: Python Evaluation
# ---------------------------------------------------------
from __future__ import print_function

text = input()

eval(text)

#---------------------------------------------------------
# PROBLEM 4: Any or All
# ---------------------------------------------------------
N = int(input())

num_list = list(map(int, input().split()))

print(
    all(i > 0 for i in num_list) and
    any(str(i) == str(i)[::-1] for i in num_list)
)

