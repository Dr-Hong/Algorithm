n = int(input())

arr = []

def setting(data):
    return data[1]

for i in range(n):
    data = input().split()
    arr.append((data[0], int(data[1])))

arr = sorted(arr, key=setting)

for student in arr:
    print(student[0], end=' ')
