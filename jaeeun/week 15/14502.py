import sys
from collections import deque
from itertools import combinations
import copy

input = sys.stdin.readline


def make_wall(cnt):
    if cnt == 3:
        bfs()
        return
    for i in range(N):
        for j in range(M):
            if r_graph[i][j] == 0:
                r_graph[i][j] = 1
                make_wall(cnt + 1)
                r_graph[i][j] = 0


def bfs():
    queue = deque()
    graph = copy.deepcopy(r_graph)

    for i in range(N):
        for j in range(M):
            if graph[i][j] == 2:
                queue.append((i, j))

    while queue:
        cur = queue.popleft()
        x = cur[0]
        y = cur[1]

        dx = [-1, 1, 0, 0]
        dy = [0, 0, -1, 1]
        for k in range(4):
            ax = x + dx[k]
            ay = y + dy[k]
            if ax < 0 or ay < 0 or ax >= N or ay >= M:
                continue
            if graph[ax][ay] == 0:
                graph[ax][ay] = 2  # 바이러스 전파
                queue.append((ax, ay))
    global result
    cnt = 0
    for i in range(N):
        for j in range(M):
            if graph[i][j] == 0:
                cnt += 1
    result = max(result, cnt)


N, M = map(int, input().split())
r_graph = [list(map(int, input().split())) for _ in range(N)]

result = 0
make_wall(0)
print(result)
