import sys

sys.setrecursionlimit(10**9)


def dfs(v):
    visited[v] = True  # 방문한 것으로 처리
    for node in arr[v]:  # 인접한 노드 방문
        if visited[node]:  # 방문했다면(True라면) continue
            continue
        dfs(node)  # 인접한 노드로 dfs 재귀 호출
        dp[v][0] += dp[node][1]  # 내가 early adaptor가 아니면 child가 early adaptor여야 함
        dp[v][1] += min(dp[node])  # 내가 early adaptor면, child가 뭐든 상관 없음


n = int(input())

visited = [False] * (n + 1)
arr = [[] for _ in range(n + 1)]
dp = [[0, 1] for _ in range(n + 1)]

for _ in range(n - 1):
    a, b = map(int, input().split())
    arr[a].append(b)
    arr[b].append(a)

dfs(1)
print(min(dp[1]))
