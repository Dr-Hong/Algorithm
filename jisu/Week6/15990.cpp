// 문제: 1,2,3 더하기 5
// 유형: 다이나믹 프로그래밍
// 난이도: 실버2

#include <iostream>
#include <stdio.h>
 
using namespace std;

long long arr[100001][4] = {0, }; // 행: 만들고 싶은 수, 열: 그전에 온 수

int main(){
    int testCase, n;
    cin >> testCase;
    
    arr[1][1] = arr[2][2] = arr[3][1] = arr[3][2] = arr[3][3] = 1;
    // 이 경우는 모두 1가지 경우의 수만 있다.

    for (int i = 4; i <= 100000; i++){
        if (i - 1 >= 0)
            arr[i][1] = (arr[i-1][2] + arr[i-1][3]) % 1000000009;
        if (i - 2 >= 0)
            arr[i][2] = (arr[i-2][1] + arr[i-2][3]) % 1000000009;
        if (i - 3 >= 0)
            arr[i][3] = (arr[i-3][1] + arr[i-3][2]) % 1000000009;
    }

    while (testCase--){
        cin >> n;
        cout << (arr[n][1] + arr[n][2] + arr[n][3]) % 1000000009 << '\n';
    }

}