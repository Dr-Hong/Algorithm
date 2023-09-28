import sys
input = sys.stdin.readline

N = int(input())
lst = list(map(int, input().split()))
cnt = -1

for i in range(N-1):
    if lst[i]<lst[i+1]:
        cnt = i
    
if cnt==-1:
    print(-1)
else:
    for i in range(cnt+1, len(lst)):
        if lst[cnt]<lst[i]:
            max = i
    lst[max], lst[cnt] = lst[cnt], lst[max]
    temp = lst[cnt+1:]
    temp = sorted(temp)
    lst = lst[0:cnt+1] + temp
    print(*lst)