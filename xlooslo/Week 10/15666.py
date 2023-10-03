n, m = map(int, input().split())

arr = list(map(int, input().split()))
arr.sort()
arr2 = []
for i in range(n):
    if arr[i] not in arr2:
        arr2.append(arr[i])
ans = []

def dfs(num, count):
    if count == m:
        print(' '.join(map(str, ans)))
        return
    
    for i in range(len(arr2)):
        if arr2[i] >= num:
            ans.append(arr2[i])
            dfs(arr2[i], count+1)
            ans.pop()

dfs(arr2[0], 0)