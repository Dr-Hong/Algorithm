n = int(input())
nums = list(map(int, input().split()))

count = 0

def isPrime(num):
    if num == 1:
        return 0
    else:
        for i in range(2, num):
            if num % i == 0:
                return 0
        return 1

for i in nums:
    if isPrime(i):
        count += 1

print(count)