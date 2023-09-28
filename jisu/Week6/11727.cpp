// 문제: 2xn 타일링2
// 유형: 다이나믹 프로그래밍
// 난이도: 실버3

#include <iostream>
using namespace std;

int main(){
    int n;
    cin >> n;
    int arr[1001] = {0, };
    arr[1] = 1;
    arr[2] = 3;
    for (int i = 3; i < n + 1 ; i++){
            arr[i] = (arr[i-1] + 2 * arr[i-2]) % 10007;
    }
    cout << arr[n] << '\n';
}