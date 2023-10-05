n, m = map(int, input().split())
board = []
arr = [[0 for j in range(m)] for i in range(n)]
for i in range(n):
    board.append(input())

for i in range(n):
    for j in range(m):
        if board[i][j] == '.':
            arr[i][j] = 0
        else:
            arr[i][j] = 1

dx = [-1, 0, 1]
ans = 0

def func(x, y):
    if y == m-1:
        return True
    
    for i in range(3):
        nx = x + dx[i]
        ny = y + 1
        
        if nx >= 0 and nx < n and arr[nx][ny] == 0:
            arr[nx][ny] = 1
            if func(nx, ny):
                return True
    return False

for i in range(n):
    if func(i, 0):
        ans += 1

print(ans)