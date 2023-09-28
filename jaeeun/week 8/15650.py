import sys

n, m = map(int, input().split())

def dfs(result):
    if len(result) == m :
        print(*result)
        return
    for i in range(1, n+1):
        if (i not in result) and (len(result)==0 or i> result[-1]):
            result.append(i)
            dfs(result)
            result.pop()

dfs([])