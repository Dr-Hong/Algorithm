# 한 자릿수: 1~9
# 두 자릿수: 10~99
# 세 자릿수: 100~999

n = input()
count = 0

for i in range(1, len(n)):
    count += int('9' + '0' * (i-1)) * i

count += (int(n) - int('1' + '0' * (len(n)-1)) + 1) * len(n)

print(count)

"""
def div(num, mul):
    if num >= 1:
        mul += 1
        return div(num/10, mul)
    else:
        return mul

n = int(input())
count = 0

for i in range(1, n+1):
    count += div(i, 0)

print(count)
"""