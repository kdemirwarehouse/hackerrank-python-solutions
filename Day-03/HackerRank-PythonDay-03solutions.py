"""
HackerRank Python Solutions - Day 3
Date: 2025-01-26
"""

# ---------------------------------------------------------
# PROBLEM 1: What's Your Name?
# ---------------------------------------------------------


def print_full_name(first, last):
    print(f"Hello {first} {last}! You just delved into python.")
if __name__ == '__main__':
    first_name = input()
    last_name = input()
    print_full_name(first_name, last_name)

# ---------------------------------------------------------
# PROBLEM 2: Mutations
# ---------------------------------------------------------
def mutate_string(string, position, character):
    return "".join([character if e == position else c for e,c in enumerate(string)])
#o anki indeks değiştirmek istediğimiz positiona eşitse characteri ekliyor,
#değilse characteri olduğu gibi bırakıyor


s = input()
i, c = input().split()
s_new = mutate_string(s, int(i), c)
print(s_new)


# ---------------------------------------------------------
# PROBLEM 3: Find a string
# ---------------------------------------------------------
def count_substring(string, sub_string):
    counter = 0
    for i, c in enumerate(string):
        if i + len(sub_string) > len(string):
            break
        if string[i:i + len(sub_string)] == sub_string:
            counter += 1
    return counter


if __name__ == '__main__':
    string = input().strip()
    sub_string = input().strip()

    count = count_substring(string, sub_string)
    print(count)

# ---------------------------------------------------------
# PROBLEM 4: Text Alignment
# ---------------------------------------------------------
#Replace all ______ with rjust, ljust or center.

thickness = int(input()) #This must be an odd number
c = 'H'

# Top Cone
for i in range(thickness):
    print((c * i).rjust(thickness - 1) + c + (c * i).ljust(thickness - 1))

# Top Pillars
for i in range(thickness + 1):
    print((c * thickness).center(thickness * 2) + (c * thickness).center(thickness * 6))

# Middle Belt
for i in range((thickness + 1) // 2):
    print((c * thickness * 5).center(thickness * 6))

# Bottom Pillars
for i in range(thickness + 1):
    print((c * thickness).center(thickness * 2) + (c * thickness).center(thickness * 6))

# Bottom Cone
for i in range(thickness):
    print(((c * (thickness - i - 1)).rjust(thickness) + c + (c * (thickness - i - 1)).ljust(thickness)).rjust(thickness * 6))


# ---------------------------------------------------------
# PROBLEM 5: Text Wrap
# ---------------------------------------------------------
import textwrap


def wrap(string, max_width):
    return "\n".join([string[i:i + max_width] for i in range(0, len(string), max_width)])


if __name__ == '__main__':
    string, max_width = input(), int(input())
    result = wrap(string, max_width)
    print(result)


