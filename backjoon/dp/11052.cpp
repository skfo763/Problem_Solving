#include <iostream>
#include <algorithm>
using namespace std;

int dp[1002];
int ptable[1002];

int main(void) {
	int i, j, count, res;
	scanf("%d", &count);

	for(i=1; i<=count; i++) {
		scanf("%d", &ptable[i]);
	}

	dp[0] = 0;
	dp[1] = ptable[1];

	for(i=2; i<=count; i++) {
		int max = 0;

		for(j=1; j<=i; j++) {
			if(max < ptable[j] + dp[i-j]) {
				max = ptable[j] + dp[i-j];
			}
		}
		dp[i] = max;
	}

	cout << dp[count] << endl;

	return 0;
}
