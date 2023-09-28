#체스판 다시 칠하기

import sys
input = sys.stdin.readline

N, M = map(int, input().split())
arr = [input().rstrip() for _ in range(N)]
# print(arr)
# print(arr[0][0])


def check(chess):
    #첫번째로 확인하지 말 것.
    cnt = 0
    if (chess[0][0]=='W'):
        for i in range(0,4):
            for j in range(0,4):
                if chess[i*2][j*2]!='W':
                    cnt += 1
        for i in range(0,4):
            for j in range(0,4):
                if chess[i*2+1][j*2+1]!='B':
                    cnt+=1

    elif (chess[0][0]=='B'):
        for i in range(0,4):
            for j in range(0,4):
                if chess[i*2][j*2]!='B':
                    cnt += 1
                if chess[i*2+1][j*2+1]!='W':
                    cnt+=1
                
    return cnt

len = M - 7 #순회하는 횟수
for k in range(len):
    for l in range(N-8):
        new_arr = []
        new_arr.append(arr[l][k:k+8])
        new_arr.append(arr[l+1][k:k+8])
        new_arr.append(arr[l+2][k:k+8])
        new_arr.append(arr[l+3][k:k+8])
        new_arr.append(arr[l+4][k:k+8])
        new_arr.append(arr[l+5][k:k+8])
        new_arr.append(arr[l+6][k:k+8])
        new_arr.append(arr[l+7][k:k+8])
        cnt = check(new_arr)
        print("새 배열 :", new_arr)
        print(cnt)