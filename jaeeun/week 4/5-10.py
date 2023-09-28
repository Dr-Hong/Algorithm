import sys

n, m = map(sys.stdin.readline().split()) 
#m * n 이면 m : 가로, n : 세로

#얼음 틀 형태로 입력 받기
ice = []
for i in range(n):
    ice.append(list(map(int, sys.stdin.readline().split())))     #input을 리스트로 변환 -> list로 mapping하여 전체 ice 배열에 append함.

#상하좌우 방문하는(방문하지 않은 노드에 한해) dfs
def dfs(x,y):
    if x <= -1 or x>= n or y <=-1 or y >= m:
        return False
    if ice[x][y] == 0:
        ice[x][y] = 1
        dfs(x-1,y)
        dfs(x+1,y)
        dfs(x,y-1)
        dfs(x,y+1)
        return True #방문하지 않았던 노드였기에, 1로 바꾼 후 True 반환
    return False

cnt = 0
for i in range(n):
    for j in range(m):
        if dfs(i,j) :
            cnt += 1

print(cnt)