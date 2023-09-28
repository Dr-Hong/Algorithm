// 실전문제: 위에서 아래로 - C++

// C++에서 STL Sort는 기본으로 오름차순 정렬이다.
// 하지만, compare 파라미터를 이용해서 콜백 함수를 선택적으로 처리할 수 있다.

#include<iostream>
using namespace std;

bool compare (int a, int b){
    return a > b;
}

int main(){
    int N;
    cin >> N;
    int A[501];
    for (int i = 0; i < N; i++){
        cin >> A[i];
    }
    sort(A,A+N,compare);
    // sort(A,A+N,greater<>());
    // greater<>() 임시 객체를 콜해서 보다 간편하게 사용할 수 있다.
    for (int i = 0; i < N; i++)
    cout << A[i] << " ";
}