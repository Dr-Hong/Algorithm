n = int(input())
array = list(map(int, input().split()))
dp = [1] * n  # 증가하는 부분 수열의 길이를 저장할 배열

for i in range(1, n):
    for j in range(0, i):
        if array[j] < array[i]:
            dp[i] = max(dp[i], dp[j]+1)
max_length = max(dp)  # 가장 긴 증가하는 부분 수열의 길이
print(max_length)

result = []  # 가장 긴 증가하는 부분 수열을 저장할 배열
max_index = dp.index(max_length)  # 가장 긴 증가하는 부분 수열의 마지막 원소의 인덱스
result.append(array[max_index])

for i in range(max_index - 1, -1, -1):  # 1씩 감소하며 0까지 역순으로 반복
    if dp[i] == max_length - 1 and array[i] < result[-1]:
        result.append(array[i])
        max_length -= 1

result.reverse()
for num in result:
    print(num, end=" ")
