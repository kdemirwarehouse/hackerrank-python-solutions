"""
HackerRank Python Solutions - Day 15
Date: 2025-02-20
Author: Kadir Demir
"""

# ---------------------------------------------------------
# PROBLEM 1: XML2-Find the Maximum Depth
# ---------------------------------------------------------
import xml.etree.ElementTree as etree

maxdepth = 0


def depth(elem, level):
    global maxdepth
    level += 1

    if level > maxdepth:
        maxdepth = level

    for child in elem:
        depth(child, level)


__name__ == '__main__':
n = int(input())
xml = ""
for i in range(n):
    xml = xml + input() + "\n"
tree = etree.ElementTree(etree.fromstring(xml))
depth(tree.getroot(), -1)

print(maxdepth)

# ---------------------------------------------------------
# PROBLEM 2: Standardize Mobile Number Using Decorators
# ---------------------------------------------------------
def wrapper(f):
    def fun(l):
        new_list = []
        for num in l:
            num = num[-10:]
            num = "+91 " + num[:5] + " " + num[5:]
            new_list.append(num)
        return f(new_list)
    return fun

@wrapper
def sort_phone(l):
    print(*sorted(l), sep='\n')

if __name__ == '__main__':
    l = [input() for _ in range(int(input()))]


