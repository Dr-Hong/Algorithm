#에디터

from sys import stdin

stack1 = list(input())      #앞쪽 stack
stack2 = []                 #뒤쪽 stack

for _ in range(int(input())):
    command = list(stdin.readline().split())
    if command[0] == 'L' and stack1:
        stack2.append(stack1.pop())
    elif command[0] == 'D' and stack2:
        stack1.append(stack2.pop())
    elif command[0] == 'B' and stack1:
        stack1.pop()
    elif command[0] == 'P':
        stack1.append(command[1])

answer = stack1 + stack2[::-1]
print(''.join(answer))
