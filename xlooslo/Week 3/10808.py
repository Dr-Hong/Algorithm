s = input()
count = [0] * 26

for i in s:
    count[ord(i) - ord('a')] += 1

for i in count:
    print(i, end=' ')