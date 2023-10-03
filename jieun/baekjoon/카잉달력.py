import sys
input = sys.stdin.readline

t = int(input())

for _ in range(t):
    m,n,x,y = map(int, input().split())
    i = x
    val = False
    while val==False and i<=m*n:
        if (i-x)%m == 0 and (i-y)%n == 0:
            print(i)
            val=True
        i+=m
    if val==False:
        print(-1)
