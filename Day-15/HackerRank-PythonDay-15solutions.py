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

# ---------------------------------------------------------
# PROBLEM 3: Decorators 2 - Name Directory
# ---------------------------------------------------------
'''sample input :
3
Mike Thomson 20 M
Robert Bustle 32 M
Andria Bustle 30 F

Sort the names from younger to older

Put "Mr." before men and "Ms." before women.
'''

import operator
def person_lister(f):
    def inner(people):
        people.sort(key=lambda x: int(x[2]))
        return (f(person) for person in people)
    return inner

@person_lister
def name_format(person):
    return ("Mr. " if person[3] == "M" else "Ms. ") + person[0] + " " + person[1]


def main():
    people = [input().split() for i in range(int(input()))]
    print(*name_format(people), sep="\n")

main()

# ---------------------------------------------------------
# PROBLEM 4: Arrays
# ---------------------------------------------------------
import numpy


def arrays(arr):
    n = numpy.array(list(reversed(arr)), float)
    return n


arr = input().strip().split(' ')
result = arrays(arr)
print(result)

# ---------------------------------------------------------
# PROBLEM 5: Numpy Shape and Reshape
# ---------------------------------------------------------

import numpy

my_num_list = input().split()

my_num_list = list(map(int, my_num_list))

my_array = numpy.array(my_num_list)

print (numpy.reshape(my_array, (3,3)))

