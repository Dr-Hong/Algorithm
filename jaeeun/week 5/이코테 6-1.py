ary = [7,5,9,0,3,1,6,2,4,8]

for i in range(len(ary)):
    min_index = i
    for j in range(i+1, len(ary)):
        if ary[min_index] > ary[j]:
            min_index = j
    ary[i], ary[min_index] = ary[min_index], ary[i]
    #이런식으로 선언해도 swap이 가능함.

print(ary)