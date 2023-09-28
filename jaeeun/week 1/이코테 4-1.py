import sys

n = int(sys.stdin.readline())
x,y = 1,1

dx = [0,0,-1,1] 
dy = [-1,1,0,0]
move = ['L','R','U','D']

plans = sys.stdin.readline().split()
for plan in plans:
    
    for i in range(len(move)):
        if plan==move[i]:
            if x + dx[i] > n or y + dy[i] > n or x + dx[i]< 1 or y + dy[i]<1:
                break
            nx = x + dx[i]
            ny = y + dy[i]
    x, y = nx, ny

print(x, " ", y)
