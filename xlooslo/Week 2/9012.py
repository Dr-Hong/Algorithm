# cannot을 append 해서 for문 바깥에서 확인하는 방식
# isValid 변수를 추가해서 이미 NO를 출력한 경우 다시 출력하지 않도록 할 수도 있다.
# string 대신 list로 입력 받고 for i in list 해도 된다.
import sys
n = int(input())

for _ in range(n):
    stk = []
    tmp = sys.stdin.readline().rstrip()
    
    for i in range(len(tmp)):
        if (tmp[i] == '('):
            stk.append('(')
        
        elif (tmp[i] == ')'):
            if stk:
                stk.pop()
            else:
                stk.append('cannot')
                break
    
    if not stk:
        print("YES")
    else:
        print("NO")