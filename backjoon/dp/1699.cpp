#include <iostream>
#include <algorithm>
using namespace std;

int dp[100010];

int main(void) {
	int i, val;
	scanf("%d", &val);

	for(int i=1; i<=val; i++) {
		for(int j=1; j*j<=i; j++) {
			if(dp[i] > dp[i-j*j]+1 || dp[i] == 0) {
				dp[i] = dp[i-j*j] + 1;
			}
		
		}
	}

	cout << dp[val];
	
	return 0;
}
