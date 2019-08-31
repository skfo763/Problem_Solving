#include <iostream>
#include <algorithm>
using namespace std;

int dp[2][1000010];
int data[2][100010];

int main(void) {
	int count, w, i, j;
	scanf("%d", &count);

	for(int k=0; k<count; k++) {

		scanf("%d", &w);

		for(i=0; i<2; i++) {
			for(j=1; j<=w; j++) {
				scanf("%d", &data[i][j]);
			}
		}

		dp[0][0] = dp[1][0] = 0;
		dp[0][1] = data[0][1];
		dp[1][1] = data[1][1];

		for(i=2; i<=w; i++) {
			dp[0][i] = max(dp[1][i-1], dp[1][i-2]) + data[0][i];
			dp[1][i] = max(dp[0][i-1], dp[0][i-2]) + data[1][i];
		}

		printf("%d\n", max(dp[0][w], dp[1][w]));
	}

	return 0;
}
