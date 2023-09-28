#BFS -> 최소경로 찾기

import sys
from collections import deque

n, m = map(int, sys.stdin.readline().split())

graph = []
for i in range(n):
    graph.append(list(map(int, sys.stdin.readline().split())))     #input을 리스트로 변환 -> list로 mapping하여 전체 ice 배열에 append함.

#상하좌우
dx = [-1,-1,0,0]
dy = [0,0,-1,1]

def bfs(x,y):
    queue = deque()
    queue.append([x,y])
    while queue:
        nx = x+dx[i]
        ny = y+dy[i]
        for i in range(4):
            if nx < 0 or ny <0 or nx >=n or ny >=m:
                continue
            if graph[nx][ny] == 0:
                continue
            if (graph[nx][ny]):       #1일 경우
                graph[nx][ny] = graph[x][y] + 1
                queue.append([nx][ny])

        return bfs(nx,ny)
    
print(bfs(0,0))