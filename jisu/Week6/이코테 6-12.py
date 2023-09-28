# 실전문제: 두 배열의 원소 교체

n, k = int(input())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

a.sort() # 내림차순
b.sort(reverse=True) # 오름차순

for i in range (k):
    if a[i] < b[i]:
        a[i] , b[i] = b[i], a[i]
    else:
        break

print(sum(a)) # 배열 A의 모든 원소의 합 출력