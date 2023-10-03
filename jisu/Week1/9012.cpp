#include <iostream>
#include <string>
#include <stack>
using namespace std;

int main(void) {
	int k;
	cin >> k;
	while (k > 0) {
		k--;
		string input;
		cin >> input;

		stack<char> st;
		string answer = "YES";
		for (int i = 0; i < input.length(); i++) {
			if (input[i] == '(') {
				st.push(input[i]);  //   스택에 '(' 저장
			}
			else if (!st.empty() && input[i] == ')' && st.top() == '(') {
				st.pop();   //  ')'가 '('와 짝이 맞는지 확인하고 pop
			}
			else {
				answer = "NO";
				break;
			}
		}
		if (!st.empty()) answer = "NO";

		cout << answer << endl;
	}
	return 0;
}