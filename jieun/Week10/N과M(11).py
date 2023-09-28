def dfs(x):
    if len(result) == m:
        print(" ".join(map(str, result)))
        return
    
    for i in num:
        result.append(i)
        dfs(i)
        result.pop()


n, m = map(int, input().split())
num = list(map(int, input().split()))
num = list(set(num))
num.sort()
result = []
dfs(0)