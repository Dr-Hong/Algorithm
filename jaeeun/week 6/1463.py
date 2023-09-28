import sys

x = int(sys.stdin.readline())
D = [0] * (x+1)
# D : 각 index가 되기 위해 연산 사용하는 최소값을 담은 리스트
D[1] = 0
for i in range(2,x+1):
    D[i] = D[i-1] + 1
    if i%2==0:
        D[i] = min(D[i], D[i//2]+1)
    if i%3==0:
        D[i] = min(D[i], D[i//3]+1)

print(D[x])