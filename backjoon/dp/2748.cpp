#include <iostream>
using namespace std;
unsigned long long dp[100];

int main(void) {
	int i, val;
	scanf("%d", &val);
	
	dp[0] = 0;
	dp[1] = 1;
	
	for(i=2; i<=val; i++) {
		dp[i] = dp[i-1] + dp[i-2];	
	}
	
	cout << dp[val] << endl;
	return 0;
}
