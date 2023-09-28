n, m = map(int, input().split())
x, y, dir = map(int, input().split())

d = [[0] * m for _ in range(n)]
d[x][y] = 1

array = []
for i in range(n):
    array.append(list(map(int, input().split())))

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

def turn_left():
    global dir
    dir -= 1
    if dir == -1:
        dir = 3

count = 1
turn = 0

while True:
    turn_left()
    nx = x + dx[dir]
    ny = y + dy[dir]
    
    if d[nx][ny] == 0 and array[nx][ny] == 0:
        count += 1
        turn = 0
        d[nx][ny] = 1
        x = nx
        y = ny
        continue
    else:
        turn += 1
    
    if turn == 4:
        x -= dx[dir]
        y -= dy[dir]
        turn = 0
        if (array[x][y] == 1):
            break

print(count)