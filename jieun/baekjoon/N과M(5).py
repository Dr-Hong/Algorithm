def dfs():
    if len(result) == m:
        print(" ".join(map(str, result)))
        return
    
    for i in num:
        if i not in result: 
            result.append(i)
            dfs()
            result.pop()

n, m = map(int, input().split())
num = list(map(int, input().split()))
num.sort()
result = []
dfs()