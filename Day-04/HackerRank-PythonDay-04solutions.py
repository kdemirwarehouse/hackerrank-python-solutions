"""
HackerRank Python Solutions - Day 4
Date: 2025-01-27
"""
import os

# ---------------------------------------------------------
# PROBLEM 1: String Validator
# ---------------------------------------------------------

if __name__ == '__main__':
    s = input()


    def validator(s):
        alnum, alpha, digits, lower, upper = False, False, False, False, False

        for c in s:
            if c.isalnum():
                alnum = True
            if c.isalpha():
                alpha = True
            if c.isdigit():
                digits = True
            if c.islower():
                lower = True
            if c.isupper():
                upper = True

        print(alnum)
        print(alpha)
        print(digits)
        print(lower)
        print(upper)


    validator(s)


# ---------------------------------------------------------
# PROBLEM 2: Designer Door Mat
# ---------------------------------------------------------

user_input = input().split()

n,m = int(user_input[0]), int(user_input[1])

s = 1

for line in range(n+1):
    if line < int(n/2):
        print((".|."*s).center(m, "-"))
        s += 2
    elif line == round(n/2):
        print("WELCOME".center(m, "-"))
    elif line > int(n/2) and s > 1:
        s -= 2
        print((".|."*s).center(m, "-"))

'''
    ---------------.|.---------------
    ------------.|..|..|.------------
    ---------.|..|..|..|..|.---------
    ------.|..|..|..|..|..|..|.------
    ---.|..|..|..|..|..|..|..|..|.---
    -------------WELCOME-------------
    ---.|..|..|..|..|..|..|..|..|.---
    ------.|..|..|..|..|..|..|.------
    ---------.|..|..|..|..|.---------
    ------------.|..|..|.------------
    ---------------.|.---------------
'''

# ---------------------------------------------------------
# PROBLEM 3: String Formatting
# ---------------------------------------------------------
def print_formatted(number):
    width = len(bin(number).replace("0b", ""))

    for i in range(1, number + 1):
        dec = str(i)

        octal = oct(i)[2:]

        hex_val = hex(i).replace("0x", "").upper()

        binary = bin(i)[2:]

        print(f"{dec:>{width}} {octal:>{width}} {hex_val:>{width}} {binary:>{width}}")


if __name__ == '__main__':
    n = int(input())
    print_formatted(n)

# ---------------------------------------------------------
# PROBLEM 4: Alphabet Rangoli
# ---------------------------------------------------------
import string


def print_rangoli(size):
    alfabe = string.ascii_lowercase #küçük harfli bütün harfler gelmesi için

    width = 4 * size - 3
    rows = []

    for i in range(size):
        kesit = alfabe[i:size]

        elemanlar = list(kesit[::-1] + kesit[1:])
        satir_metni = "-".join(elemanlar)

        rows.append(satir_metni.center(width, "-"))

    tam_desen = rows[::-1] + rows[1:]
    print("\n".join(tam_desen))


if __name__ == '__main__':
    n = int(input())
    print_rangoli(n)

# ---------------------------------------------------------
# PROBLEM 5: Capitalize!
# ---------------------------------------------------------

def solve(s):
    return " ".join((word.capitalize()for word in s.split(" ")))

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = solve(s)

    fptr.write(result + '\n')

    fptr.close()