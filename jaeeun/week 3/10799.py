import sys

x = sys.stdin.readline()
stack = []
cnt = 0

s = len(x)

for i in range(s):
    if x[i] == '(': stack.append('(')
    elif x[i] == ')':
        if  x[i-1]== '(': 
            #레이저 생김
            cnt += len(stack) - 1
            stack.pop()
        else:
            #쇠막대기의 끝이므로, 잘린 부분이 늘어남 -> +1
            cnt += 1
            stack.pop()

print(cnt)
