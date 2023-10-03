#스택수열

import sys
n = int(sys.stdin.readline())

stack=[]
result=[]
flag = 0    #가능/불가능 판단하는 변수
cur = 1     #스택에 현재 넣고 있는 정수

for i in range(n):
    num = int(sys.stdin.readline())     #수열에 넣고자 하는 수, 해당 수가 나올 때까지 stack에 push함.
    while cur<=num: 
        stack.append(cur)
        result.append("+")
        cur+=1      #스택에 오름차순으로 push. 입력한 수(수열에 넣고자 하는 수)를 만나면 while문을 나가게 된다.

    if stack[-1] == num :   #수열에 넣고자 하는 수가 TOP에 있는 경우, 스택에서 pop
        stack.pop()
        result.append("-")
    else:                   #스택의 TOP이 수열에 넣고자 하는 수가 아닐 경우, 조건 성립 안함.
        print("NO")
        flag=1
        break

if flag == 0:
    for k in result:
        print(k)
