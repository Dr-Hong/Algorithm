import sys
from collections import deque  # deque모듈로 큐 구현


t = int(input())  # 테스트케이스 개수

for _ in range(t):
    n = int(input())  # 체스판 한변의 길이
    now = list(map(int, sys.stdin.readline().split()))  # 현재 위치
    dest = list(map(int, sys.stdin.readline().split()))  # 목표 위치

    matrix = [[0] * n for _ in range(n)]  # 이동한 횟수
    visited = [[False] * n for _ in range(n)]

    queue = deque()

    # 시계방향
    dx = [-2, -1, 1, 2, 2, 1, -1, -2]
    dy = [1, 2, 2, 1, -1, -2, -2, -1]

    def bfs():
        queue.append(now)  # 시작위치 큐에 추가
        visited[now[0]][now[1]]  # 시작위치 방문함

        while queue:
            x, y = queue.popleft()  # 큐의 가장 앞 원소 꺼내기

            if x == dest[0] and y == dest[1]:
                return 0

            for i in range(8):
                nx = x + dx[i]
                ny = y + dy[i]

                if nx < 0 or nx >= n or ny < 0 or ny >= n:
                    continue

                if nx == dest[0] and ny == dest[1]:  # 원하는 위치라면
                    visited[nx][ny] = True
                    return matrix[x][y] + 1  # 이동한 횟수+1

                if visited[nx][ny] == False:  # 방문하지 않았고 원하는 위치가 아니라면
                    queue.append([nx, ny])
                    visited[nx][ny] = True
                    matrix[nx][ny] = matrix[x][y] + 1

    answer = bfs()
    print(answer)
