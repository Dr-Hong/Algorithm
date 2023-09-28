import sys

n = int(sys.stdin.readline())

for _ in range(n):
    stack = []
    s = input()
    i, vps = 0, 0
    for ch in s:
        if ch == "(":
            stack.append('(')
        elif ch == ")":
            if stack:
                stack.pop()
            else:
                vps = 1
                break
    if not stack and vps == 0:
        print("YES")
    elif stack or vps == 1:
        print("NO")
