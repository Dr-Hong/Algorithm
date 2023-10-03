n, m = map(int, input().split())
arr = list(map(int, input().split()))
arr.sort()
ans = []

def dfs(num, count):
    if count == m:
        print(' '.join(map(str, ans)))
        return
    
    for i in range(n):
        if arr[i] >= num:
            ans.append(arr[i])
            dfs(arr[i], count + 1)
            ans.pop()

dfs(arr[0], 0)