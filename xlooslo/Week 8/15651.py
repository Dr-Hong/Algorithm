n, m = map(int, input().split())
arr = []

def dfs(count):
    if count - 1 == m:
        print(' '.join(map(str, arr)))
        return
    
    for i in range(1, n+1):
        arr.append(i)
        dfs(count+1)
        arr.pop()

dfs(1)