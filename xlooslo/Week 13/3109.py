# 입력 예제는 다 올바르게 나오지만
# 2 5
# . . . . .
# . . . . .
# 입력하면 0이 나온다.

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
    global ans
    if y == m-1:
        ans += 1
        return
    
    for i in range(3):
        nx = x + dx[i]
        ny = y + 1
        
        if nx >= 0 and nx < n and arr[nx][ny] == 0:
            arr[nx][ny] = 1
            func(nx, ny)
            break

for i in range(n):
    func(i, 0)

print(ans)