// 요세푸스 문제
// N,K가 주어지면 (N, K) 요세푸스 순열을 구하는 프로그램 작성
// 원형 큐를 이용하면 쉽게 풀이 가능

#include <iostream>
#include <queue>
using namespace std;

int main(){
    int N = 0;
    int K = 0;

    cin >> N >> K;

    queue<int>Q;
    for (int i = 1; i <= N; i++) Q.push(i);

    cout << "<";

    while (Q.size() > 1) { // 마지막에는 , 를 출력하지 않아야 하므로
		for (int i = 1; i < K; i++) {
			int temp = Q.front();
			Q.pop();
			Q.push(temp);
		}
		cout << Q.front() << ", ";
		Q.pop();
	}
	cout << Q.front() << ">\n";

}