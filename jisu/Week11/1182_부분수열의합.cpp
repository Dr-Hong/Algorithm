#include<iostream>
#include<algorithm>
#include<vector>

using namespace std;

int N, Sum;
int Ans = 0;
vector<int> arr;

void solve(int idx, int tmp) {
	if (idx == N) return; // idx N-1 까지 탐색한 경우 종료
	if (tmp + arr[idx] == Sum) Ans++; // return을 안함에 주의

	solve(idx + 1, tmp); // idx 수를 더하지 않는 경우
	solve(idx + 1, tmp + arr[idx]); // idx 수를 더하는 경우
}

int main() {
	cin >> N >> Sum;

	for (int i = 0; i < N; i++) {
		int tmp;
		cin >> tmp;
		arr.push_back(tmp);
	}

	solve(0, 0);
	cout << Ans;

	return 0;
}