import sys
n = int(sys.stdin.readline())
dp = [x for x in range(0,n+1)]

for i in range(1, n+1):
    for j in range(1, i+1):
        if j*j > i:
            break
        if dp[i-j*j]+1 < dp[i]:
            dp[i] = dp[i-j*j] +1
            
print(dp[n])