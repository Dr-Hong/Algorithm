import sys

n = int(sys.stdin.readline())
students = []

for i in range(n):
    student = input().split()
    key = student[0]
    value = student[1]
    students.append((key,value))

students = sorted(students, key = lambda student : student[1])

for i in students:
    print(i[0], end = ' ')