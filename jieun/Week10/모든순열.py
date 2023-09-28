def dfs(x):
    if len(result) == n:
        print(" ".join(map(str, result)))
    for i in range(1, n+1):
        if i not in result:
            result.append(i)
            dfs(i)
            result.pop()

n = int(input())
result=[]
dfs(1) #1부터 시작