#include <iostream>

long dp[110][11];

int main(void) {
	int a;
	scanf("%d", &a);

	for(int i=1; i<=9; i++) {
		dp[1][i] = 1;
	}
	
	for(int i=2; i<=a; i++) {
		for(int j=0; j<=9; j++) {
			if(j == 0) {
				dp[i][j] = dp[i-1][j+1];
			} else if(j == 9) {
				dp[i][j] = dp[i-1][j-1];
			} else {
				dp[i][j] = (dp[i-1][j-1] + dp[i-1][j+1]) % 1000000000;
			}
		}
	}
	
	long ans = 0;
	for(int i=0; i<=9; i++) {
		ans += dp[a][i];
	}

	printf("%ld\n", ans % 1000000000);

	return 0;
}
