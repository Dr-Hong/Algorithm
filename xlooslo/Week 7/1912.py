import sys

n = int(input())
inputData = list(map(int, sys.stdin.readline().split()))

maxData = inputData[0]

for i in range(1, n):
    inputData[i] = max(inputData[i], inputData[i] + inputData[i-1])

for i in range(1, n):
    maxData = max(maxData, inputData[i])

print(maxData)