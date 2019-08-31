#include <iostream>

long dp[1010][11];

int main(void) {
	int a;
	scanf("%d", &a);

	for(int i=0; i<=9; i++) {
		dp[1][i] = 1;
	}

	for(int i=2; i<=a; i++) {
		for(int j=0; j<=9; j++) {
			long temp = 0;
			for(int k=j; k<=9; k++) {
				temp += dp[i-1][k] % 10007;
			}
			
			dp[i][j] = temp % 10007;
		}
	}

	long res = 0;
	for(int i=0; i<=9; i++) {
		res += dp[a][i] % 10007;
	}

	printf("%ld", res % 10007);
}
