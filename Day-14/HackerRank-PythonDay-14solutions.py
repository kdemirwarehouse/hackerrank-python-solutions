"""
HackerRank Python Solutions - Day 14
Author: Kadir Demir
Date: 2026-02-19
"""

# ---------------------------------------------------------
# PROBLEM 1: HTML Parser - Part 1
# ---------------------------------------------------------
from html.parser import HTMLParser

N = int(input())

class MyHTMLParser(HTMLParser):
    def handle_starttag(self, tag, attrs):
        print("Start :", tag)
        if attrs:
            for element in attrs:
                attribute_name = element[0]
                attribute_value = element[1]
                print(f"-> {attribute_name} > {attribute_value}")

    def handle_endtag(self, tag):
        print("End   :", tag)

    def handle_startendtag(self, tag, attrs):
        print("Empty :", tag)
        if attrs:
            for element in attrs:
                attribute_name = element[0]
                attribute_value = element[1]
                print(f"-> {attribute_name} > {attribute_value}")

parser = MyHTMLParser()

for _ in range(N):
    current_line = input()
    if parser.feed(current_line):
        print(parser.feed(current_line))

# ---------------------------------------------------------
# PROBLEM 2: HTML Parser - Part 2
# ---------------------------------------------------------
from html.parser import HTMLParser


class MyHTMLParser(HTMLParser):

    def handle_data(self, data):
        if data != "\n":
            print(">>> Data")
            print(data)

    def handle_comment(self, data):
        lst = data.split("\n")
        if (len(lst) == 1):
            print(">>> Single-line Comment")
            print(lst[0])
        else:
            print(">>> Multi-line Comment")
            print(*lst, sep="\n")


html = ""
for i in range(int(input())):
    html += input().rstrip()
    html += '\n'

parser = MyHTMLParser()
parser.feed(html)
parser.close()

# ---------------------------------------------------------
# PROBLEM 3: Detect HTML Tags, Attributes and Attribute values
# ---------------------------------------------------------
from html.parser import HTMLParser


class MyHTMLParser(HTMLParser):
    def handle_starttag(self, tag, attrs):
        print(tag)
        for attr in attrs:
            print("-> " + attr[0] + " > " + attr[1])


parser = MyHTMLParser()
for _ in range(int(input())):
    parser.feed(input())

# ---------------------------------------------------------
# PROBLEM 4: XML 1 - Find the Score
# ---------------------------------------------------------
import sys
import xml.etree.ElementTree as etree


def get_attr_number(node):
    count = len(node.attrib)

    for child in node:
        count += get_attr_number(child)

    return count


if __name__ == '__main__':
    sys.stdin.readline()
    xml = sys.stdin.read()
    tree = etree.ElementTree(etree.fromstring(xml))
    root = tree.getroot()
    print(get_attr_number(root))

# ---------------------------------------------------------
# PROBLEM 5: Validating UID
# ---------------------------------------------------------
import re

for _ in range(int(input())):
    S = input()
    # t = re.search(r"^[a-zA-Z0-9]{10}$",S)
    # t = re.search(r"[A-Z][0-9a-z]*[A-Z]",S)
    # t = re.search(r"\d[A-Za-z]*\d[A-Za-z]*\d",S)
    # t = re.search(r"([A-Za-z0-9])[A-Za-z0-9]*(?=\1)",S)

    if (re.search(r"^[a-zA-Z0-9]{10}$", S)):
        if (re.search(r"[A-Z][0-9a-z]*[A-Z]", S)):
            if (re.search(r"\d[A-Za-z]*\d[A-Za-z]*\d", S)):
                if (re.search(r"([A-Za-z0-9])[A-Za-z0-9]*(?=\1)", S)):
                    print("Invalid")

                else:
                    print("Valid")
            else:
                print("Invalid")
        else:
            print("Invalid")
    else:
        print("Invalid")




