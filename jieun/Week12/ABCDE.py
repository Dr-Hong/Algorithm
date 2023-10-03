import sys


def dfs(idx, friend):
    if friend == 4:  # 관계가 성립하는 경우
        print(1)
        exit()

    visited[idx] = True

    for i in arr[idx]:  # 친구관계인 노드 확인
        if not visited[i]:
            dfs(i, friend + 1)

    visited[idx] = False


n, m = map(int, input().split())
arr = [[] for i in range(n)]
visited = [False] * n
for _ in range(m):
    a, b = map(int, input().split())
    arr[a].append(b)
    arr[b].append(a)

for i in range(n):
    dfs(i, 0)

print(0)
