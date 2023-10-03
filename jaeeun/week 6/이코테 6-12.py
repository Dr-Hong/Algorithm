import sys

n, k = map(int, sys.stdin.readline().split())
A = sys.stdin.readline().split()
B = sys.stdin.readline().split()

#A의 최소값과 B의 최대값을 바꿔치기 하도록.
A.sort()
B.sort(reverse=True)

for i in range(k):
    if A[i] < B[i] :
        A[i], B[i] = B[i], A[i]
    else:
        break

sum = 0
for j in A:
    sum += int(j)

print(sum)