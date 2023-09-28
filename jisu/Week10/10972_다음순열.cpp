#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

bool next_permutation(vector<int> &a, int n){
    int i = n - 1; // 인덱스는 n-1 까지 있으므로 -1을 해줌
    while (i > 0 && a[i - 1] > a[i]){ // 어디까지가 내림차순인지 확인
        i--;
    } // i번부터 내림차순 시작 (i ~ n-1)

    if (i <= 0) return false; // 마지막 순열(모두 오름차순)인 경우 false 반환

    int j = n - 1;
    while (a[j] <= a[i-1]){ // 내림차순 바로 앞의 숫자(i-1)보다 처음으로 큰 수 찾기
        j--;
    } // j = 처음으로 큰 수
    swap(a[j],a[i-1]); // 두 수 스왑하기

    int k = n-1;
    while (i < k){ // 오름차순 변경
        swap(a[i], a[k]);
        i++;
        k--;
    }
    return true;
}

int main(){
    ios::sync_with_stdio(0);
    cin.tie(0);
    cout.tie(0);

    int N;
    cin >> N; // 수 입력받기
    vector<int> arr(N);
    for (int i = 0; i < N; i++)
        cin >> arr[i]; // 순열 입력받기

    if (next_permutation(arr, N)){ // 다음 순열이 있는 경우, 다음 순열 출력
        for (int i = 0; i < N; i++)
            cout << arr[i] << ' ';
        cout << "\n";
    }
    else cout << "-1"; // 다음 순열이 없는 경우, -1 출력
}