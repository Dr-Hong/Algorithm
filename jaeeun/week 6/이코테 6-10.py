import sys

n = int(sys.stdin.readline())

array = []
for i in range(n):
    array.append(int(sys.stdin.readline()))

array = sorted(array, reverse=True)

for i in array:
    print(i, end = ' ')