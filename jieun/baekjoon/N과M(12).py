def dfs(x):
    if len(result) == m:
        print(" ".join(map(str, result)))
        return
    
    for i in range(x, len(num)):
        result.append(num[i])
        dfs(i)
        result.pop()

n, m = map(int, input().split())
num = sorted(list(set((map(int, input().split())))))

result = []
dfs(0)