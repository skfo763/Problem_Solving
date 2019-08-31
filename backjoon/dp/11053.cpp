#include <iostream>
using namespace std;

int dp[1010];

int main(void) {
	int i, count, min, j;
	int max = 0;
	scanf("%d", &count);
	int *data = new int [count + 1];

	for(i=1; i<=count; i++) {
		scanf("%d", &data[i]);
	}

	dp[0] = 0;
	for(i=1; i<=count; i++) {
		int min = 0;
		for(j=0; j<i; j++) {
			if(data[j] < data[i]) {
				if(dp[j] > min) min = dp[j];
			}
		}

		dp[i] = dp[min]+1;
		if(max < dp[i]) max = dp[i];
	}

	printf("%d\n", max);

	delete [] data;
	return 0;
}
