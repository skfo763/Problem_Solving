#include <iostream>
#include <stdlib.h>

unsigned long long dp[1001];

unsigned long long get_k(unsigned long long x) {
	if(x==1) {
		return 1;
	} else if(x==2) {
		return 3;
	} else if(dp[x] != 0) {
		return dp[x];
	} else {
		return dp[x] = (2*get_k(x-2) + get_k(x-1))%10007;
	}
}


int main(void) {
	int a;
	scanf("%d", &a);
	printf("%llu\n", get_k(a));

	return 0;
}
