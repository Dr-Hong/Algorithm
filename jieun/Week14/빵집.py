def pipe(i, j):
    if j == c-1:
        return True
    
    for d in dx:
        if 0<=i+d<r and table[i+d][j+1] == '.' and not visited[i+d][j+1]:
            visited[i+d][j+1] = True
            if pipe(i+d, j+1):
                return True
    return False

r, c = map(int, input().split())
table = [list(input().rstrip()) for _ in range(r)]

visited = [[False] * c for _ in range(r)]
dx = [-1, 0, 1]
count = 0

for i in range(r):
    if table[i][0] == '.':
        if pipe(i, 0):
            count += 1
print(count)