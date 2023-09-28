ans = []
visited = [False] * 10
maxAns = 0
minAns = 9999999999

n = int(input())
arr = input().split()

def checking(i, j, k):
    if k == '<':
        return i < j
    else:
        return i > j

def dfs(count):
    global maxAns, minAns
    if count == n+1:
        maxAns = max(maxAns, int(''.join(map(str, ans))))
        minAns = min(minAns, int(''.join(map(str, ans))))
        return
    
    for i in range(10):
        if not visited[i]:
            if count == 0 or checking(ans[-1], i, arr[count-1]):
                visited[i] = True
                ans.append(i)
                dfs(count+1)
                ans.pop()
                visited[i] = False

dfs(0)

print(str(maxAns).zfill(n+1)) 
print(str(minAns).zfill(n+1))