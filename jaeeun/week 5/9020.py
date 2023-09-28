import sys

def is_prime(n):
    cnt = 0
    for i in range(n):
        if cnt>=2: return False
        if n%(i+1) == 0 :
            cnt += 1
    if (cnt==2):    #1과 자기자신으로만 나누어 떨어지는 경우 -> 소수임
        return True
    

tc = int(sys.stdin.readline())      #테스트 케이스의 개수

for i in range(tc):
    x = int(sys.stdin.readline())
    p = int(x/2)
    for i in range(p):
        if is_prime(p + i) and is_prime(p - i):
            print(p-i, p+i)
            break
        else:
            continue