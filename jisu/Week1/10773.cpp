#include <iostream>
#include <stack>
using namespace std;

int main() {
	stack<int> s;
	int K;
	int num;
	int stack_size;
	int sum = 0;

	cin >> K;

	for (int i = 0; i < K; i++) {
		cin >> num;	
		if (num == 0) {	
			s.pop();	// 0이면 pop
		}
		else
			s.push(num); // 0이 아니면 push
	}

	stack_size = s.size();
	for (int i = 0; i < stack_size; i++) {
		sum += s.top();	// 하나씩 더하기
		s.pop();
	}

	cout << sum;

	return 0;
}