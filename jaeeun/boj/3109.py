import sys
input = sys.stdin.readline

def dfs(x, y):
    global cnt
    visited[x][y] = True
    if y==C-1:
        cnt+=1
        return True
    for dx in [-1,0,1]:
        ax = x + dx
        ay = y + 1
        if 0<=ax<R and 0<=ay<C:
            if graph[ax][ay] !="x" and not visited[ax][ay]:
                if dfs(ax,ay):
                    return True
    return False

cnt = 0
R, C = map(int,input().split())
graph = [list(input().strip()) for _ in range(R)]
visited = [[False for i in range(C)] for k in range(R)]

for p in range(R):
    dfs(p,0)

print(cnt)