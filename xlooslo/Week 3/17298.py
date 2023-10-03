from sys import stdin

n = int(input())
arr = list(map(int, stdin.readline().split()))
answer = [-1] * n
stack = []

for i in range(n):
    while stack and arr[i] > arr[stack[-1]]:
        answer[stack.pop()] = arr[i]
    stack.append(i)

while stack:
    answer[stack.pop()] = -1

print(*answer)