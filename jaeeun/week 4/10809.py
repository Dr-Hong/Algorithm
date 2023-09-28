import sys

S = input().rstrip()

cnt = 0
out = [-1] * 26

for x in S:
    if (out[ord(x)-97] == -1): out[ord(x) - 97] = cnt
    cnt+=1

for y in out:
    print(y, " ")