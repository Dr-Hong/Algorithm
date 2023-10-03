import sys
import heapq
input = sys.stdin.readline

n, k = map(int, input().split()) 
jew = [] #모든 보석의 무게와 가격 저장 -> 무게 기준 최소힙으로 유지

for i in range(n):
    m, v = map(int, input().split())
    heapq.heappush(jew, [m, v])

c = [int(input()) for _ in range(k)]
c.sort() #가벼운 것부터 무거운 순으로 정렬

answer = 0
tmp = [] #가방에 담을 수 있는 보석들 저장 -> 가격 기준 최대힙으로 유지

for i in c: #가벼운 것부터 무거운 순
    while jew and jew[0][0]<=i: #가방에 담을 수 있는 최대 무게(i)보다 가벼운 보석들을 모두 담기
        heapq.heappush(tmp, -jew[0][1])  # tmp에 보석의 가치를 음수로 저장하여 최대힙을 만들기
        heapq.heappop(jew)  # 처리한 보석은 jew에서 제거
    if tmp:
        answer -= heapq.heappop(tmp) #tmp에서 가장 비싼 보석을 꺼내서 answer에서 그 가격을 더하기
    elif not jew:
        break
print(answer)