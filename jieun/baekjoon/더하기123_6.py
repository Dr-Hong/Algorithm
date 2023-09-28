n = int(input())

dp = [[0] * 4 for _ in range(100001)]

dp[1][1] = 1
dp[2][1] = 1
dp[2][2] = 1
dp[3][1] = 1
dp[3][3] = 1

for i in range(4, 100001):
    dp[i][1] = sum(dp[i-2]) % 1000000009
    dp[i][2] = sum(dp[i-4]) % 1000000009
    dp[i][3] = sum(dp[i-6]) % 1000000009
    if i == 4 or i == 6:
        dp[i][0] = (dp[i][0] + 1) % 1000000009

for j in range(n):
    num = int(input())
    print(sum(dp[num]) % 1000000009)
