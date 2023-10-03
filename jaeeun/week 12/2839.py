import sys
input = sys.stdin.readline

N = int(input())
k = N//5
min_cnt = 0

if N==3:
    min_cnt = 1
elif N == 4:
    min_cnt = -1
elif N%5==0:
    min_cnt = N//5
else:
    for i in range(0,k+1):
        if (N-5*i)%3==0:
            min_cnt = i+(N-5*i)//3
    if min_cnt == 0:
        min_cnt = -1

print(min_cnt)