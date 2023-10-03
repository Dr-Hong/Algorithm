n = int(input())

num = list(map(int, input().split()))
find = False

for i in range(n-1, 0, -1):

    if num[i-1] > num[i]: #앞값이 뒷값보다 큰 경우
        for j in range(n-1, 0, -1):
            if num[i-1] > num[j]:
                num[i-1], num[j] = num[j], num[i-1]
                num = num[:i] + sorted(num[i:],reverse=True) #내림차순정렬
                find = True
                break

    if find:
        print(" ".join(map(str, num)))
        break

if not find:
    print(-1)
