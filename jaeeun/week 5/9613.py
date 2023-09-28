import sys
import math
#math.gcd() 함수를 사용할 것이다.

n = int(sys.stdin.readline())

for i in range(n):
    result=0
    m = (sys.stdin.readline().split())   #m[1] ~ m[]
    #조합을 만드는 알고리즘??
    #0,1 0,2 0,3 ... 0,n
    for k in range(1, len(m)):
        for j in range(k+1, len(m)):
            result += math.gcd(int(m[k]),int(m[j]))
    print(result)