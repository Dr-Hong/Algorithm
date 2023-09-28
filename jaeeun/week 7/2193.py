import sys

n = int(sys.stdin.readline())
dp = [1,1]
#print(dp)

for i in range(2, 91):
    dp.append(dp[i-2]+dp[i-1])

print(dp[n-1])