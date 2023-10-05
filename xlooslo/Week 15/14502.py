from collections import deque
import copy

n, m = map(int, input().split())
board = [0 for _ in range(n)]
for i in range(n):
    board[i] = list(map(int, input().split()))

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

def makeWall(count):
    if count == 3:
        bfs()
        # 어쩌고 저쩌고
        return
    for i in range(n):
        for j in range(m):
            if board[i][j] == 0:
                board[i][j] = 1
                makeWall(count+1)
                board[i][j] = 0

def bfs():
    queue = deque()
    tmp = copy.deepcopy(board)

    for i in range(n):
        for j in range(m):
            if board[i][j] == 2:
                queue.append((i, j))

    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx, ny = x+dx[i], y+dy[i]
            if nx<0 or nx>=n or ny<0 or ny>=m:
                continue
            if tmp[nx][ny] == 0:
                tmp[nx][ny] = 2
                queue.append((nx, ny))
    
    count = 0
    for i in range(n):
        for j in range(m):
            if tmp[i][j] == 0:
                count += 1
    
    global result
    result = max(result, count)


result = 0
makeWall(0)


print(result)