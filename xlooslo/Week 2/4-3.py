loc = input()
col = int(ord(loc[0]) - ord('a') + 1)
row = int(loc[1])

steps = [(1, 2), (2, 1), (2, -1), (1, -2), (-1, -2), (-2, -1), (-2, 1), (-1, 2)]
count = 0

for step in steps:
    next_col = col + step[1]
    next_row = row + step[0]
    
    if next_col>=1 and next_col<=8 and next_row>=1 and next_row<=8:
        count += 1

print(count)