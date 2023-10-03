// 실전문제: 두 배열의 원소 교체

#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

int main(){
    int N, K;
    vector<int> v1;
    vector<int> v2;
    long long ans = 0; // 합의 결과가 매우 클 수 있으므로 long long 으로 선언한다.

    cin >> N >> K;
    for (int i = 0; i < N; i++){
        int tmp;
        cin >> tmp;
        v1.push_back(tmp);
    }for (int i = 0; i < N; i++){
        int tmp;
        cin >> tmp;
        v2.push_back(tmp);
    }

    sort(v1.begin(), v1.end()); // 작은거 3개 골라야 하므로 내림차순 정렬
    sort(v2.begin(), v2.end(), greater<int>()); // 큰거 3개 골라야 하므로 오름차순 정렬

    for (int i = 0; i < K; i++){
        if (v1[i] < v2[i]){
            swap(v1[i],v2[i]);
        }
        else break;
    }

    for (int i = 0; i < N; i++)
        ans += v1[i];

    cout << ans;
    return 0;
}