# List 슬라이싱으로 구현하려고 했으나 시간복잡도 때문에 불가능한 문제
# Stack 이용해서 접근하기

import sys
str1 = list(sys.stdin.readline().rstrip())
str2 = []
n = int(sys.stdin.readline())

for _ in range(n):
    tmp = sys.stdin.readline().split()

    if (tmp[0] == 'P'):
        str1.append(tmp[1])
    
    elif (tmp[0] == 'B'):
        if str1:
            str1.pop()
    
    elif (tmp[0] == 'D'):
        if str2:
            str1.append(str2[-1])
            str2.pop()
            
    elif (tmp[0] == 'L'):
        if str1:
            str2.append(str1[-1])
            str1.pop()
            
print(''.join(str1+str2[::-1]))