# 17298 오큰수 문제를 먼저 푸는 게 좋다.
from collections import Counter
from sys import stdin

n = int(stdin.readline())
arr = list(map(int, stdin.readline().split()))
stk = []
ans = [-1] * n
count = Counter(arr)

# 처음 접근했던 방식이지만 시간 초과가 난다.
# count = [0] * n

#for i in arr:
#    count[i] += 1

for i in range(n):
    while stk and count[arr[stk[-1]]] < count[arr[i]]:
        ans[stk.pop()] = arr[i]
    stk.append(i)

print(*ans)