import sys

command = input()

move = [(-2,-1),(-2,1),(-1,-2),(-1,2),(1,-2),(1,2),(2,-1),(2,1)]

#전부 정수 형태로 변환
col = ord(command[0])-96
row = ord(command[1])-48
print(col,row)

sol = 0
for step in move:
    if (8>=(row+step[0])>0) and (8>=(col+step[1])>0) :
        sol+=1
    else:
        continue

print(sol)