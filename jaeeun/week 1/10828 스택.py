#push -> append
#pop -> pop
#size -> len
#empty -> bool로 판단
#top -> 
import sys
sys.stdin = open('/Users/jaeeun/Algorithm-Study/jaeeun/week 1/10828tc1.txt', 'r')
n = int(sys.stdin.readline())

stack = []

for i in range(n):
    command = sys.stdin.readline().split()
    if command[0] == 'push':
        stack.append(command[1])
    elif command[0] == 'pop':
        if not stack :
            print("-1")
        else:
            print(stack[len(stack)-1])
            stack.pop()
    elif command[0] == 'size':
        print(len(stack))
    elif command[0] == 'empty':
        if not stack: print("1")
        else:print("0")
    elif command[0] == 'top':
        if not stack : print("-1")
        else : print(stack[-1])
