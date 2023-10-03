#N과 M(10)
import sys
input = sys.stdin.readline

N, M = map(int, input().split())
lst = sorted(list(map(int, input().split())))
temp = []
result = []
isUsed = [0] * N

def dfs(temp,idx):
    if len(temp)==M:
        print(*temp)
        return
    num = 0
    for i in range(idx, N):
        if not isUsed[i] and lst[i]!=num:
            temp.append(lst[i])
            num = lst[i]
            isUsed[i] = 1
            dfs(temp,i+1)
            temp.pop()
            isUsed[i] = 0

dfs(temp,0)