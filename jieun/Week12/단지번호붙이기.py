dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

n = int(input())

arr = []
for _ in range(n):
    row = input()
    row_list = [int(char) for char in row]
    arr.append(row_list)


def dfs(x, y):
    global count
    if x < 0 or x >= n or y < 0 or y >= n:  # 범위에서 벗어나는 경우
        return False

    if arr[x][y] == 1:  # 집이 있는 경우
        count += 1  # 집의 개수 += 1
        arr[x][y] = 0
        for i in range(4):  # 상하좌우로 집이 있는지 확인
            nx = x + dx[i]
            ny = y + dy[i]
            dfs(nx, ny)
        return True
    return False


count = 0
home = []  # 각 단지의 집 수
for i in range(n):
    for j in range(n):
        if dfs(i, j):  # 집이 존재한다면
            home.append(count)  # home 배열에 집의 개수 추가
            count = 0  # 집의 개수 초기화

home.sort()  # 집의 개수를 오름차순으로 정렬
print(len(home))
for i in home:
    print(i)
