// 문제: 합분해
// 유형: 다이나믹 프로그래밍
// 난이도: 골드5

#include<iostream>
using namespace std;
typedef long long ll;
#define MAX 201
#define Moduler 1000000000

int main(void){
    ios::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);

    int N, K;
    ll DP[MAX][MAX];
 
    cin >> N >> K;

    for (int i = 0; i <= N; i++)
        DP[1][i] = 1; // 1개의 수만 이용해서 N을 만드는 경우는 1가지 경우
 
    for (int k = 2; k <= K; k++){
        for (int n = 0; n <= N; n++){
            for (int i = 0; i <= n; i++){
                DP[k][n] += DP[k - 1][i];} // 점화식 DP[k][n] = DP[k-1][0] + ... + DP[k-1][n]
            DP[k][n] = DP[k][n] % Moduler;
        }
    }
 
    cout << DP[K][N] << endl;
 
    return 0;
}