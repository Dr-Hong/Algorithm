// 최대공약수와 최소공배수

using namespace std;
#include <iostream>

int gcd(int a, int b) { //최대 공약수
	int r = a % b;

	while (r != 0) {
		a = b;
		b = r;
		r = a % b;
	}
	return b;
}

int lcm(int a, int b) { //최소 공배수
	return (a * b) / gcd(a, b);
}

int main(void) {

	int a, b;

	cin >> a >> b;

	cout << gcd(a, b) << endl;
	cout << lcm(a, b) << endl;

	return 0;
}