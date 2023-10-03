// 문제: 가장 긴 증가하는 부분 수열
// 유형: 다이나믹 프로그래밍
// 난이도: 실버2

// dp 배열의 각 인덱스마다 해당 수를 포함할 경우 만들 수 있는 배열의 가장 긴 길이를 저장한다

#include <iostream>
using namespace std;

int max(int a, int b){
    return (a > b) ? a : b;
}

int main(){
    ios::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);

    int N;
    int arr[1002];
    int dp[1002];
    int ans = 0;
    cin >> N;

    for (int i = 1; i <= N; i++){
        cin >> arr[i];
    }

    for (int i = 1; i <= N; i++){
        dp[i] = 1; // 현재 i 번째 수 하나를 선택하는 경우
        for (int j = i - 1; j >= 1; j--){ // i 번째 수보다 작은 경우에서 가장 긴 배열의 길이 탐색
            if (arr[i] > arr[j]){
                dp[i] = max(dp[i], dp[j] + 1); // dp[i]의 최대값 구하기
            }
        }
        ans = max(dp[i],ans);
    }
    
    cout << ans;

    return 0;

}