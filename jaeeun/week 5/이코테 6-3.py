ary = [7,5,9,0,3,1,6,2,4,8]

for i in range(1, len(ary)):
    for j in range(i, 0, -1):
        if ary[j]<ary[j-1]:
            ary[j-1], ary[j] = ary[j], ary[j-1]
        else:
            break

print(ary)
