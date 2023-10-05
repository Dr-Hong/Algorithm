n = int(input())
for i in range(n):
    t = int(input())
    arr = [0 for _ in range(t)]
    
    for j in range(t):
        arr[j] = list(map(int, input().split()))
    
    arr.sort()
    tmp = arr[0][1]
    count = 1
    
    for j in range(1, t):
        if arr[j][1] < tmp:
            tmp = arr[j][1]
            count += 1
    
    print(count)