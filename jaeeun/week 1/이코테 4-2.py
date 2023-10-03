import sys

n,p = map(int, sys.stdin.readline().split())

count = 0
for i in range (n+1):   #시간별로 카운트
    for j in range (60):
        for k in range (60):
            if str(p) in str(k)+str(i)+str(j):
                count+=1



print(count)