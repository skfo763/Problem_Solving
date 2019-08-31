#include <iostream>
#include <algorithm>
using namespace std;

int dp[10010];

int main(void) {
	int i, count;
	scanf("%d", &count);
	int *data = new int [count + 1];

	for(i=1; i<=count; i++) {
		scanf("%d", &data[i]);
	}

	dp[0] = 0; dp[1] = data[1]; dp[2] = data[1] + data[2];

	for(i=3; i<=count; i++) {
		dp[i] = max(max(dp[i-3]+data[i-1]+data[i], dp[i-1]), dp[i-2]+data[i]);
	}

	printf("%d\n", dp[count]); 
}
