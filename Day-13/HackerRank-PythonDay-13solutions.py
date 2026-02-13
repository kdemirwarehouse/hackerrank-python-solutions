"""
HackerRank Python Solutions - Day 8
Date: 2026-02-10
"""
# ---------------------------------------------------------
# PROBLEM 1: Re.findall() & Re.finditer()
# ---------------------------------------------------------
import re

pattern = r"(?<=[^AEIOUaeiou])([AEIOUaeiou]{2,})(?=[^AEIOUaeiou])"

S = re.findall(pattern, input())

if S:
    print(*S, sep = "\n")
else:
    print(-1)

# ---------------------------------------------------------
# PROBLEM 2: Validating Roman Numerals
# ---------------------------------------------------------

regex_pattern = r"^M{0,3}(CM|CD|D?C{0,3})(XC|XL|L?X{0,3})(IX\IV\V?I{0,3}$"

import re

print(str(bool(re.match(regex_pattern, input()))))

# ---------------------------------------------------------
# PROBLEM 3: Validating and Parsing Email Addresses
# ---------------------------------------------------------
import re
import email.utils

pattern = r"[a-zA-Z][\w\.-]*@[a-zA-Z]+\.[a-zA-Z]{1,3}"
N = int(input())

for _ in range(N):
    email = email.utils.parseaddr(input())
    if re.fullmatch(pattern, email):
        print(email.utils.formataddr((email[0], email[1])))


# ---------------------------------------------------------
# PROBLEM 4: Validating phone numbers
# ---------------------------------------------------------

import re
N = int(input())

pattern = r"[7-9][0-9]{9}"

for _ in range(N):
    phone_num = input()
    if re.fullmatch(pattern, phone_num):
        print("YES")
    else:
        print("NO")

# ---------------------------------------------------------
# PROBLEM 5: Hex Color Code
# ---------------------------------------------------------

import re

for i in range(int(input())): # In this case the only valid color codes we want happen on lines that end in a semi colon
    match = re.findall(r"(#[a-f0-9]{3,6})[\;\,\)]{1}", input(), re.I) #ignore case, since hex is both capital and lowercase
    if match:
        for j in list(match):
            print(j)




