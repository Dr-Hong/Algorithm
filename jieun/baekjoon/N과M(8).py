def dfs(x):
    if len(result) == m:
        print(" ".join(map(str, result)))
        return
    
    for i in range(x, n):
        result.append(num[i])
        dfs(i)
        result.pop()

n, m = map(int, input().split())
num = list(map(int, input().split()))
num.sort()
result = []
dfs(0)