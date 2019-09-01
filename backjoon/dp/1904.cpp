#include <iostream>
#include <algorithm>
using namespace std;

unsigned long dp[1000001];

int main(void) {
	int i, val;
	scanf("%d", &val);

	dp[0] = dp[1] = 1;
	for(i=2; i<=val; i++) {
		dp[i] = (dp[i-1] + dp[i-2]) % 15746;
	}

	cout << dp[val] % 15746;
	return 0;
}
