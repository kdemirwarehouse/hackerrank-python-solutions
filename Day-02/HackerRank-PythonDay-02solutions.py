"""
HackerRank Python Solutions - Day 2
Date: 2025-01-25
"""

# ---------------------------------------------------------
# PROBLEM 1: Finding the percentage
# ---------------------------------------------------------

n = int(input())
student_marks = {}

for _ in range(n):
    name, *line = input().split()
    scores = list(map(float, line))
    student_marks[name] = scores
query_name = input()

def find_percentage(name):
    return f"{sum(student_marks[name]) / len(student_marks[name]):.2f}"

print(find_percentage(query_name))



# ---------------------------------------------------------
# PROBLEM 2: Lists
# ---------------------------------------------------------

N = int(input())
the_list = list()

for _ in range(N):
    query = input().split()
    if query[0] == "print":
        print(the_list)
    elif query[0] == "insert":
        the_list.insert(int(query[1]), int(query[2]))
    elif query[0] == "remove":
        the_list.remove(int(query[1]))
    elif query[0] == "append":
        the_list.append(int(query[1]))
    elif query[0] == "sort":
        the_list = sorted(the_list)
    elif query[0] == "pop":
        the_list.pop()
    elif query[0] == "reverse":
        the_list.reverse()


# ---------------------------------------------------------
# PROBLEM 3: Tuples
# ---------------------------------------------------------

n = int(input())
integer_list = map(int, input().split())
t = tuple(integer_list)
print(hash(t))

# ---------------------------------------------------------
# PROBLEM 4: Swapcase()
# ---------------------------------------------------------

def swap_case(s):
    return s.swapcase()

if __name__ == '__main__':
    s = input()
    result = swap_case(s)
    print(result)

# ---------------------------------------------------------
# PROBLEM 5: Split & Join
# ---------------------------------------------------------


