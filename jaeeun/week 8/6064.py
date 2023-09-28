import sys
input = sys.stdin.readline

t = int(input())

for _ in range(t):
    m, n, x, y = map(int, input().split())
    k = x
    valid = False
    while not valid and (k <= m*n):
        if (k-x)%m == 0 and (k-y)%n == 0:
            valid = True
            print(k)
        k+=m
    if not valid:
        print(-1)