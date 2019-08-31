#include <iostream>
#include <algorithm>
using namespace std;

int dp[50];

int main(void) {
	int count, i, j;
	scanf("%d", &count);
	
	dp[0] = 1;
	dp[1] = 0;
	dp[2] = 3;

	for(i=2; i<=count; i++) {
		
		int res = 3*dp[i-2];
		
		for(j=3; j<=i; j++) {
			if(i%2 == 0) {
				res += 2*dp[i-j];
			}
		
		}

		dp[i] = res;
	}

	cout << dp[count] << endl;

	return 0;
}
