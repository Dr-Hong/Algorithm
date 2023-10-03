def dfs(x):
    global max_diff
    if x == n:
        diff = 0
        for i in range(0, n-1):
            diff += abs(arr[i] - arr[i+1])
        max_diff = max(max_diff, diff)
        return
    for i in range(n):
        if not visited[i]:
            visited[i] = 1
            arr.append(A[i])
            dfs(x + 1)
            visited[i] = 0
            arr.pop()

n = int(input())
A = list(map(int, input().split()))
visited = [0] * n
arr = []
max_diff = 0  
dfs(0)
print(max_diff)