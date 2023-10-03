# 1107번 리모컨
n = int(input())
m = int(input())

if m > 0:
    button = set(map(int, input().split(" ")))
else:
    button = set()

# 현재 채널에서 +, -만 사용하여 이동하는 경우
min_count = abs(100 - n)

for num in range(1000001):
    #0부터 num 시작
    num = str(num)

    for i in range(0, len(num)):

        #num이 고장난 숫자인지 확인
        if int(num[i]) in button:
            break

        #num이 고장나지 않은 숫자일 경우
        elif i == len(num)-1:
            min_count = min(min_count, abs(int(num)-n)+len(num))
print(min_count)