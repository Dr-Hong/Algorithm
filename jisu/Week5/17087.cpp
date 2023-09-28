// 17087번: 숨바꼭질 6

#include <iostream>
using namespace std;

int gcd(int num1, int num2){
    if (num2==0)return num1;
    else return gcd(num2, num1%num2);
}

int main(){
    int N, S; // 동생 N명, 수빈이의 현재 위치 S
    cin >> N >> S;
    int distance[100001]; // 동생과 수빈이의 거리
    for (int i = 0; i < N; i++){
        cin >> distance[i];
        if (S > distance[i])    distance[i] = S - distance[i]; // 양수가 되도록 한다
        else    distance[i] = distance[i] - S;
    }
    if (N == 1) cout << distance[0];
    else if (N == 2)    cout << gcd(distance[0], distance[1]);
    else {
        int result = gcd(distance[0], distance[1]);
        for (int i = 2; i < N; i ++){
            result = gcd(result,distance[i]);
        }
        cout << result;
    }
}