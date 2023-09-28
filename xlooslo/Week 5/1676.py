n = int(input())
factorial = 1
count = 0

for i in range(1, n+1):
    factorial *= i

factorial = str(factorial)
factorial = list(map(int, factorial))

while factorial:
    if factorial[-1] != 0:
        print(count)
        break
    else:
        factorial.pop()
        count += 1
        if not factorial:
            print(count)