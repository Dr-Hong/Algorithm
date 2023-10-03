from itertools import permutations

n = int(input())
arr = list(map(int, input().split()))
p = list(permutations(arr, n))

ans = 0
for i in p:
    sum = 0
    for j in range(n-1):
        sum += abs(i[j] - i[j+1])
    ans = max(ans, sum)

print(ans)