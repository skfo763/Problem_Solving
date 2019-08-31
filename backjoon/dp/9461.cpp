#include <iostream>
#include <algorithm>
#include <cstring>
using namespace std;

unsigned long long dp[200];

int main(void) {
	int i, j, count;
	
	dp[1]=1; dp[1]=1; dp[2]=1; dp[3]=1; dp[4]=2; dp[5]=2;
	
	for(j=6; j<=100; j++) {
		dp[j] = dp[j-1] + dp[j-5];
	}

	scanf("%d", &count);
	
	while(count--) {
		int val;
		scanf("%d", &val);
		
		printf("%lld\n", dp[val]);
	}

	return 0;
}
