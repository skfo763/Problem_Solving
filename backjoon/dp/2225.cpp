#include <iostream>
#include <algorithm>
using namespace std;

long dp[201][201];

int main(void) {
	int i, j, val, min;
	scanf("%d %d", &val, &min);
	
	for(i=1; i<=200; i++) {
		for(j=1; j<=200; j++) {
			if(i==1) dp[i][j]=1;
			if(j==1) dp[i][j]=i;
		 	else {
				 dp[i][j] = (dp[i-1][j] + dp[i][j-1])%1000000000;
			}
		}

	}

	printf("%ld\n", dp[min][val]); 

	return 0;
}
