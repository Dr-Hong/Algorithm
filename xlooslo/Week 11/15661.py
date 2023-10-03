import sys
ans = sys.maxsize
input = sys.stdin.readline

n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]
visited = [False] * n

def func():
    global ans
    start, link = 0, 0
    
    for i in range(n):
        for j in range(n):
            if visited[i] and visited[j]:
                start += arr[i][j]
            elif not visited[i] and not visited[j]:
                link += arr[i][j]
    ans = min(ans, abs(start - link))
    return

def dfs(count):
    if count == n:
        func()
        return
    visited[count] = True
    dfs(count+1)
    visited[count] = False
    dfs(count+1)

dfs(0)
print(ans)