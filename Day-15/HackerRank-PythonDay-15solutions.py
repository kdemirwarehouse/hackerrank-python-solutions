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

print(maxdepth
