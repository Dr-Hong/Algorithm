// 17298번: 오큰수

#include <iostream>
#include <stack>
using namespace std;

int A[1000001]; // 오큰수를 저장하는 배열
int main()
{
    ios_base::sync_with_stdio(0);
    cin.tie(0);

    int N;
    cin >> N; // 배열의 크기 입력받기
    stack<int> st; // -1을 출력하는 경우의 배열 A의 인덱스를 저장하는 스택
    for (int i = 0; i < N; i++) {
        int num;
        cin >> num; // 수 입력받기
        A[i] = num;
        while (true) { // 스택이 비어있는 경우, push
            if (st.empty()) {
                st.push(i);
                break;
            }
            if (num > A[st.top()]) { // 오큰수일 경우 num을 넣어주고 pop
                A[st.top()] = num;
                st.pop();
            }
            else { // num이 작거나 같으면 push
                st.push(i);
                break;
            }
        }
    }
    while (!st.empty()) { // 스택에 남아 있는 index에는 -1을 넣어줌
        A[st.top()] = -1;
        st.pop();
    }
    for (int i = 0; i < N; i++) { // 오큰수 출력
        cout << A[i] << ' ';
    }
    return 0;
}
