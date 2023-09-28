import sys

n = int(sys.stdin.readline())

for i in range(n):
    quote = sys.stdin.readline().split()

    for word in quote :
        print(word[::-1], end=' ')
    print()
