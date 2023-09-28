import sys

n, m = map(int, sys.stdin.readline().split())

x, y, direction = map(int, sys.stdin.readline().split())

# n x m 형태의 방문지도 생성
visited = [[0 for j in range(m)] for i in range(n)]

#캐릭터가 위치한 좌표는 방문 처리
visited[x][y] = 1

#전체 맵 정보 입력받기 (바다, 육지)
array=[]
for i in range(n):      #행마다 채우기
    array.append(list(map(int, sys.stdin.readline().split())))

# 대각선 방향으로는 움직이지 않고, 동서남북 방향만 있으므로 같은 index에서 하나는 무조건 0임.
dx = [-1,0,1,0]
dy = [0,1,0,-1]

################################

#왼쪽으로 회전하는 함수
def turn_left():
    global direction
    direction -= 1      # 북, 서, 남, 동 순으로. 따라서 1씩 빼준다
    if direction == -1 :
        direction = 3       #서쪽으로 초기화

cnt = 1
turn_cnt = 0
while True :
    turn_left()
    nx = x + dx[direction]
    ny = y + dy[direction]
    if (visited[nx][ny]==0) and (array[nx][ny]==0):      #방문한적  없는 경우 -> 전진
        visited[nx][ny] = 1
        x = nx
        y = ny
        cnt += 1
        turn_cnt = 0
        continue
    else:       #접근 불가능한 경우
        turn_cnt += 1
    #네 방향 모두 접근해본 경우
    if turn_cnt == 4:
        nx = x - dx[direction]
        ny = y - dy[direction]
        if array[nx][ny] == 0:
            x = nx
            y = ny
        else:   # 바다인 경우
            break
        turn_cnt = 0

print(cnt)


