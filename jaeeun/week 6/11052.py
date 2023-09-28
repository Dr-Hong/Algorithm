import sys

n = int(sys.stdin.readline())
p = list(map(int, input().split()))
#p는 개수에 접근할 때 index로 해야 함.
p.insert(0,0)
#dp : 계속해서 업데이트 되는, 해당 인덱스 카드 구매할 때 최댓값
dp = [0] * (n+1)

for i in range(1, n+1):
    for j in range(1, i+1):
        #이중 포문 -> dp[i-1]+p[1], dp[i-2]+p[2]
        #이 과정에서 0번째 index를 접근하지 않으므로 (0,0) insert해줌
        dp[i] = max(dp[i-j] + p[j], dp[i])

print(dp[n])