
import sys


def promising(i):
    for x in range(i):
        if board[x] == board[i] or i-x == abs(board[i]-board[x]):
            return False
    return True


def nqueen(i):
    global count
    if i == n:
        count += 1
        return

    for j in range(n):
        if visited[j]:
            continue
        board[i] = j
        if promising(i):
            visited[j] = True
            nqueen(i+1)
            visited[j] = False


n = int(sys.stdin.readline())
count = 0
board = [0]*n
visited = [False] * n
nqueen(0)
print(count)
