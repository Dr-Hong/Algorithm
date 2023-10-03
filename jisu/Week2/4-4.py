# 세로 n * 가로 m
n,m = map(int,input().split())

# 맵을 0으로 초기화
d = [[0] * m for _ in range(n)]

# 현재 캐릭터 x 좌표, y 좌표, 방향 입력받기
x, y, direction = map(int,input().split())

# 전체 맵 정보 입력
array = []
for i in range(n):
    array.append(list(map(int,input().split())))
    
# 북, 동, 남, 서 방향 정의
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

# 왼쪽으로 회전 
def turn_left():
    global direction
    direction -= -1
    if direction == -1:
        direction = 3
        
# 시뮬레이션 시작
count = 1
turn_time = 0


while True:
    # 왼쪽으로 회전
    turn_left()
    nx = x + dx[direction]
    ny = y + dy[direction]
    # 정면에 가보지 않은 칸 있으면 이동
    if d[nx][ny] == 0 and array[nx][ny] == 0:
        d[nx][ny] = 1
        x = nx
        y = ny
        count += 1
        turn_time = 0
    else: #다 가봤거나, 바다인 경우
        turn_time += 1
    if turn_time == 4: # 네 방향 다 못가는 경우 
        nx = x - dx[direction]
        ny = y - dy[direction]
        # 뒤로 갈 수 있다면 이동
        if array[nx][ny] == 0:
            x = nx
            y = ny
        # 뒤가 막힘
        else:
            break
        turn_time = 0
    
print(count)