def dfs(num, count):
    if count == 6:
        print(*ans)
        return
    
    for i in range(1, n+1):
        if arr[i] > num:
            ans.append(arr[i])
            dfs(arr[i], count+1)
            ans.pop()

ans = []
n = 0

while True:
    arr = list(map(int, input().split()))
    n = arr[0]
    
    if n == 0:
        break
    
    dfs(0, 0)
    print('')