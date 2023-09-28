def dfs(x):
    if len(result) == m:
        print(" ".join(map(str, result)))
        return
    
    for i in range(x, n):
        if num[i] not in result: 
            result.append(num[i])
            dfs(i+1)
            result.pop()

n, m = map(int, input().split())
num = list(map(int, input().split()))
num.sort()
result = []
dfs(0)