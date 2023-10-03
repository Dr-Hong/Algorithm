#include<cstdio>
#include<algorithm>
using namespace std;

int n;
int dice[6];
int min3 = 151, min2 = 101, min1 = 51, max1 = 0;
long long answer = 0; // 타입 주의

int main() {
	scanf("%d", &n);
	for (int i = 0; i < 6; i++) {
		scanf("%d", &dice[i]);
		answer += dice[i];
		max1 = max(max1, dice[i]);
	}

	if (n == 1) {
		printf("%lld", answer - max1);
		return 0;
	}

	for (int i = 0; i < 6; i++) {
		min1 = min(min1, dice[i]);
		for (int j = i + 1; j < 6; j++) {
			if (i + j == 5) {
				continue;
			}
			min2 = min(min2, dice[i] + dice[j]);
			for (int k = j + 1; k < 6; k++) {
				if (j + k == 5 || k + i == 5) {
					continue;
				}
				min3 = min(min3, dice[i] + dice[j] + dice[k]);
			}
		}
	}

	answer = 0;
	answer += (5 * (long long)n*n - 16 * n + 12) * min1;
	answer += 4 * min3;
	answer += (8 * n - 12) * min2;

	printf("%lld", answer);
	return 0;
}