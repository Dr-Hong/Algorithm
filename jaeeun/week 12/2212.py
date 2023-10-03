import sys
input = sys.stdin.readline

N = int(input())
K = int(input())
sensors = sorted(map(int,input().split()))


if K>=N:
    print(0)
else:
    distance = []
    for i in range(len(sensors)-1):
        distance.append(abs(sensors[i+1]-sensors[i]))

    for i in range(K-1):
        distance.remove(max(distance))

    print(sum(distance))