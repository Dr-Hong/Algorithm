import sys
n = int(sys.stdin.readline())

for _ in range(n):
    str = input()
    str += " "
    stack = []

    for i in str:
        if i != " ":
            stack.append(i)
        else:
            while stack:
                print(stack.pop(), end = "")
            print(" ", end = "")
    print("")