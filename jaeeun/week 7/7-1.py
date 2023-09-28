def sequentialSearch(n, target, arr):
    for i in range(n):
        if arr[i] == target:
            return i + 1

inputData = input().split()
n = int(inputData[0])
target = inputData[1]

arr = input().split()

print(sequentialSearch(n, target, arr))