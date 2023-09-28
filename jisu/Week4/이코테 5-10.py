import sys

n, m = map(sys.stdin.readline().split()) 

# 2차원 리스트의 맵 정보 입력받기
ice = []
for i in range(n):
    ice.append(list(map(int, sys.stdin.readline().split())))

# DFS로 특정한 노드를 방문한 뒤에 연결된 모든 노드들도 방문
def dfs(x,y):
    if x <= -1 or x>= n or y <=-1 or y >= m:
        return False
    if ice[x][y] == 0:
        ice[x][y] = 1
        dfs(x-1,y)
        dfs(x+1,y)
        dfs(x,y-1)
        dfs(x,y+1)
        return True
    return False

cnt = 0
for i in range(n):
    for j in range(m):
        if dfs(i,j) :
            cnt += 1

print(cnt)