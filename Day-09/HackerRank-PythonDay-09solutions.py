"""
HackerRank Python Solutions - Day 8
Date: 2026-02-04
"""

# ---------------------------------------------------------
# PROBLEM 1: Power - Mod Power
# ---------------------------------------------------------
a = int(input())
b = int(input())
m = int(input())
print(pow(a,b))
print(pow(a,b,m))


# ---------------------------------------------------------
# PROBLEM 2: Set .difference() Operation
# ---------------------------------------------------------
eng_nums = int(input())

eng_subs = set(input().split())

fr_nums = int(input())

fr_subs = set(input().split())

print(len(eng_subs.difference(fr_subs)))


# ---------------------------------------------------------
# PROBLEM 3: Integers Come In All Sizes
# ---------------------------------------------------------
a = int(input())
b = int(input())
c = int(input())
d = int(input())

print(pow(a,b) + pow(c,d))

# ---------------------------------------------------------
# PROBLEM 4: Integers Come In All Sizes
# ---------------------------------------------------------
def get_subs():
    return input().split()

def main():
    eng_subs = set(get_subs())

    fr_subs = set(get_subs())

    print(len(eng_subs ^ fr_subs))

main()
# ---------------------------------------------------------
# PROBLEM 5:Set Mutations
# ---------------------------------------------------------

def mut_ops(A):
    m = int(input())

    for _ in range(m):
        op_name, _ = input().split()
        other_set = set(map(int, input().split()))

        if op_name == "intersection_update":
            A.intersection_update(other_set)

        elif op_name == "update":
            A.update(other_set)

        elif op_name == "symmetric_difference_update":
            A.symmetric_difference_update(other_set)

        elif op_name == "difference_update":
            A.difference_update(other_set)

    return sum(A)

def main():
    n = int(input())

    A = set(map(int,input().split()))

    result = mut_ops(A)

    print(result)

main()