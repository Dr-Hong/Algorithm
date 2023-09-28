# 1406번: 에디터 구현
# 커서를 기준으로 왼쪽 스택, 오른쪽 스택 두 개로 나누어 담음
# append, pop을 통해 할 수 있으므로 O(1)시간의 연산을 보장함

import sys

stack_l = list(input())
stack_r = []
n = int(input())

for i in range(n):
    command = sys.stdin.readline().split()

    if command[0] == "L" and stack_l:
        stack_r.append(stack_l.pop())
    elif command[0] == "D" and stack_r:
        stack_l.append(stack_r.pop())
    elif command[0] == "B" and stack_l:
        stack_l.pop()
    elif command[0] == "P":
        stack_l.append(command[1])

print("".join(stack_l + list(reversed(stack_r))))