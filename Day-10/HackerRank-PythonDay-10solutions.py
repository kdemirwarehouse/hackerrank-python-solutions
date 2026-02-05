# ---------------------------------------------------------
# PROBLEM 1: The Captain's Room
# ---------------------------------------------------------
K = int(input())

room_list = list(map(int, input().split()))

a_dict = {}

for r in room_list:
    if r in a_dict:
        a_dict[r] += 1
    else:
        a_dict[r] = 1

for r in a_dict:
    if a_dict[r] != K:
        print(r)
        break
# ---------------------------------------------------------
# PROBLEM 2: Check Subset
# ---------------------------------------------------------
T = int(input())

for _ in range(T):
    k = int(input())
    A = set(map(int, input().split()))

    l = int(input())
    B = set(map(int, input().split()))

    if A.issubset(B):
        print(True)
    else:
        print(False)
# ---------------------------------------------------------
# PROBLEM 3: Check Strict Superset
# ---------------------------------------------------------
A = set(map(int, input().split()))

n = int(input())

is_superset_strict = True

for _ in range(n):
    other_set = set(map(int, input().split()))
    if not (A > other_set):
        is_superset_strict = False
        break

print(is_superset_strict)

# ---------------------------------------------------------
# PROBLEM 4: Zipped!
# ---------------------------------------------------------
N, X = map(int, input().split())

marks = []

for _ in range(X):
    marks.append(list(map(float, input().split())))

for student in zip(*marks):
    mark_average = sum(student) / X
    print(mark_average)

# ---------------------------------------------------------
# PROBLEM 5: Zipped!
# ---------------------------------------------------------