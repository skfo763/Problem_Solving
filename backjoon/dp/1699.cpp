#include <iostream>
#include <algorithm>
#include <utility>
#define MAX 2147384000
using namespace std;

int dp[100001];

int main(void) {
	int i, j, val, min;
	scanf("%d", &val);
	dp[0] = 0; dp[1] = 1;
	
	for(i=2; i<=val; i++) {
		for(j=1; j*j<=i; j++) {
			if(dp[i-(j*j)] < dp[i] || dp[i] == 0) {
				dp[i] = dp[i-(j*j)] + 1;
			}
		}
	}

	cout << dp[val];
	
	return 0;
}
