def dfs(x, total_profit):
    global profit
    if x == n:
        profit = max(profit, total_profit)
        return
    
    if possible[x]: # 날짜 초과하지 않는 경우
        # x일에 상담을 한 경우
        dfs(x + t[x], total_profit + p[x])
        
        # x일에 상담을 하지 않은 경우
        dfs(x + 1, total_profit)

    else: # 날짜 초과하는 경우
        dfs(x + 1, total_profit)

n = int(input())
t = []
p = []
possible = [True] * n

for i in range(n):
    ti, pi = map(int, input().split())
    t.append(ti)
    p.append(pi)

for i in range(n):
    if i + t[i] > n: # n일 안에 상담을 끝낼 수 없는 경우
        possible[i] = False

profit = 0
dfs(0, 0)

print(profit)