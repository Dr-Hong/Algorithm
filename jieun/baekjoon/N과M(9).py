def dfs(x):
    prev = 0
    if len(result) == m:
        print(" ".join(map(str, result)))
        return
    
    for i in range(n):
        if not visited[i] and num[i] != prev:
            result.append(num[i])
            prev = num[i]
            visited[i] = True
            dfs(i)
            result.pop()
            visited[i] = False

n, m = map(int, input().split())
num = list(map(int, input().split()))
num.sort()

result = []
visited = [False] * n
dfs(0)