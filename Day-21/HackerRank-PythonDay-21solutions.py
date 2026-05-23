"""
HackerRank Python Solutions - Day 21
Date: 2025-05-04
"""

# ---------------------------------------------------------
# PROBLEM 1: Triangle Quest
# ---------------------------------------------------------
for i in range(1, int(input())):
    print(i * (10**i - 1) // 9

# ---------------------------------------------------------
# PROBLEM 2: Classes: Dealing with Complex Numbers
# ---------------------------------------------------------
import math
class Complex(object):
    def __init__(self, real, imaginary):
        self.real = real
        self.imaginary = imaginary
        
    def __add__(self, no):
        return Complex(
            self.real + no.real,
            self.imaginary + no.imaginary
        )

    def __sub__(self, no):
         return Complex(
            self.real - no.real,
            self.imaginary - no.imaginary
        )

    def __mul__(self, no):
        return Complex(
            self.real * no.real - self.imaginary * no.imaginary,
            self.real * no.imaginary + self.imaginary * no.real
        )

    def __truediv__(self, no):
        denominator = no.real**2 + no.imaginary**2

        return Complex(
            (
                self.real * no.real +
                self.imaginary * no.imaginary
            ) / denominator,

            (
                self.imaginary * no.real -
                self.real * no.imaginary
            ) / denominator
        )


    def mod(self):
        
        return Complex(
            math.sqrt(
                self.real**2 +
                self.imaginary**2
            ),
            0
        )


    def __str__(self):
        if self.imaginary == 0:
            result = "%.2f+0.00i" % (self.real)

        elif self.real == 0:
            if self.imaginary >= 0:
                result = "0.00+%.2fi" % (self.imaginary)
            else:
                result = "0.00-%.2fi" % (abs(self.imaginary))

        elif self.imaginary > 0:
            result = "%.2f+%.2fi" % (
                self.real,
                self.imaginary
            )

        else:
            result = "%.2f-%.2fi" % (
                self.real,
                abs(self.imaginary)
            )

        return result
if __name__ == '__main__':
    c = map(float, input().split())
    d = map(float, input().split())
    x = Complex(*c)
    y = Complex(*d)
    print(*map(str, [x+y, x-y, x*y, x/y, x.mod(), y.mod()]), sep='\n')


# ---------------------------------------------------------
# PROBLEM 3: Athlete Sort
# ---------------------------------------------------------
n, m = map(int, input().split())

athletes = []

for _ in range(n):
    row = list(map(int, input().split()))
    athletes.append(row)

k = int(input())

athletes.sort(key=lambda x: x[k])

for athlete in athletes:
    print(*athlete)

# ---------------------------------------------------------
# PROBLEM 4: gnitroS
# ---------------------------------------------------------
s = input()

lowercase = []
uppercase = []
odd_digits = []
even_digits = []

for char in s:
    if char.islower():
        lowercase.append(char)
    elif char.isupper():
        uppercase.append(char)
    else:
        if int(char) % 2 == 1:
            odd_digits.append(char)
        else:
            even_digits.append(char)

lowercase.sort()
uppercase.sort()
odd_digits.sort()
even_digits.sort()

print("".join(lowercase + uppercase + odd_digits + even_digits))

# ---------------------------------------------------------
# PROBLEM 5: Validating Email Addresses With a Filter
# ---------------------------------------------------------
def fun(s):
    try:
        username, rest = s.split("@")
        website, extension = rest.split(".")
    except ValueError:
        return False

    if username == "" or website == "" or extension == "":
        return False

    if not username.replace("-","").replace("_","").isalnum():
        return False

    if not website.isalnum():
        return False

    if not extension.isalpha():
        return False

    if len(extension) > 3:
        return False

    return True

def filter_mail(emails):
    return list(filter(fun, emails))

if __name__ == '__main__':
    n = int(input())
    emails = []
    for _ in range(n):
        emails.append(input())

filtered_emails = filter_mail(emails)
filtered_emails.sort()
print(filtered_emails)

