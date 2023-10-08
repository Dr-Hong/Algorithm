# 14502 연구소
import copy
from collections import deque

# 벽 : 조합? dfs? 삼중 for문? -> dfs로 해보자..
wall_count = 0
def set_wall(wall_count):
    if wall_count == 3: # 벽을 3개 다 세운 경우에 bfs()호출 후, return
        bfs()
        return
    for i in range(n):
        for j in range(m):
            if arr[i][j] == 0:
                arr[i][j] = 1
                set_wall(wall_count+1)
                arr[i][j] = 0

def bfs():
    global ans
    tmp = copy.deepcopy(arr) #깊은 복사
    count = 0
    # tmp[i][j] == 2인 좌표를 queue에 저장
    for i in range(n):
        for j in range(m):
            if tmp[i][j] == 2:
                q.append([i, j])
    
    # 바이러스 주변으로 퍼뜨리기
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x+dx[i]
            ny = y+dy[i]
            if 0<=nx<n and 0<=ny<m and tmp[nx][ny] == 0:
                tmp[nx][ny] = 2
                q.append([nx,ny])
    
    #0인 좌표의 개수 세기
    for i in range(n): 
        for j in range(m):
            if tmp[i][j] == 0: 
                count+=1

    ans = max(ans, count)


n, m = map(int, input().split())
arr = [[0]*n for i in range(n)]
q = deque()
ans = 0

for i in range (n):
    arr[i] = list(map(int, input().rstrip().split()))

#상하좌우 순서
dx = [0,0,-1,1] 
dy = [1,-1,0,0]

set_wall(0)
print(ans)

