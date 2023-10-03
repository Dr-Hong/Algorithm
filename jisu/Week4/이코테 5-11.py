import sys
from collections import deque

n, m = map(int, sys.stdin.readline().split())

graph = []
for i in range(n):
    graph.append(list(map(int, sys.stdin.readline().split())))     #input을 리스트로 변환 -> list로 mapping하여 전체 ice 배열에 append함.

# 이동할 네 방향 정의 (상,하,좌,우)
dx = [-1,-1,0,0]
dy = [0,0,-1,1]

# BFS 소스코드 구현
def bfs(x,y):
    queue = deque()
    queue.append([x,y])
    while queue: # 큐가 빌 때 까지 반복
        x, y = queue.popleft()
        # 현재 위치에서 네 방향으로의 위치 확인
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            # 미로 찾기 공간을 벗어난 경우 무시
            if nx < 0 or ny < 0 or nx >= n or ny >= m:
                continue
            if graph[nx][ny] == 0: continue
            if graph[nx][ny] == 1:
                graph[nx][ny] = graph[x][y] + 1
                queue.append((nx,ny))
        # 가장 오른쪽 아래까지의 최단 거리 반환
        return bfs(nx,ny)
    
print(bfs(0,0))