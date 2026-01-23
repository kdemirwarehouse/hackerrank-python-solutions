"""
HackerRank Python Solutions - Day 1
Date: 2025-01-23
"""

# ---------------------------------------------------------
# PROBLEM 1: Say "Hello, World!" With Python
# ---------------------------------------------------------
def hello_world():
    my_string = "Hello, World!"
    print(my_string)

# ---------------------------------------------------------
# PROBLEM 2: Python If-Else (Weird or Not Weird)
# ---------------------------------------------------------
def if_else_check():
    n = int(input().strip())
    # 1 <= n <= 100 kısıtlaması genellikle input aşamasında kabul edilir
    if n % 2 != 0:
        print("Weird")
    else:
        if 2 <= n <= 5:
            print("Not Weird")
        elif 6 <= n <= 20:
            print("Weird")
        elif n > 20:
            print("Not Weird")

# ---------------------------------------------------------
# PROBLEM 3: Arithmetic Operators
# ---------------------------------------------------------
def arithmetic_operators():
    a = int(input())
    b = int(input())
    print(a + b)
    print(a - b)
    print(a * b)

# ---------------------------------------------------------
# PROBLEM 4: Python: Division
# ---------------------------------------------------------
def python_division():
    a = int(input())
    b = int(input())
    print(a // b)
    print(a / b)

# ---------------------------------------------------------
# PROBLEM 5: Loops (Square of Numbers)
# ---------------------------------------------------------
def loops_square():
    n = int(input())
    for i in range(n):
        print(i ** 2)

if __name__ == '__main__':
    # Buraya hangi fonksiyonu test etmek istiyorsan onu yazabilirsin
    # Örn: loops_square()
    pass