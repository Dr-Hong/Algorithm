#include <iostream>
#include <algorithm>
using namespace std;

int main(){
    int arr[9];
    int sum = 0;
    for (int i = 0; i < 9; i++){
        cin >> arr[i]; // 난쟁이 키 입력받기
        sum += arr[i];
    }

    sort(arr, arr+9); // 오름차순 정렬

    for (int i = 0; i < 8; i++){
        for (int j = 1; j < 9; j++){
            if (sum - arr[i] - arr[j] == 100){ // 가짜 난쟁이 판별
                for (int k = 0; k < 9; k++){
                    if (k != i && k != j) // 가짜 난쟁이 뺴고 출력
					    cout << arr[k] << '\n';
                }
                return 0;
            }
        }
    }
    return 0;
}