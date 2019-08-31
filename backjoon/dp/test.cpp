#include <iostream>
#include <algorithm>
#include <utility>
#define MAX 2147384000
using namespace std;

int dp[1000001];
int cs[3];

int main(void) {
	int i, count;
	dp[1] = 0;
	scanf("%d", &count);

	for(i=2; i<=count; i++) {
		cs[0] = cs[1] = cs[2] = MAX;

		if(i%3 == 0) {
			cs[0] = dp[i/3];
		}

		if(i%2 == 0) {
			cs[1] = dp[i/2];
		}

		cs[2] = dp[i-1];
		
		dp[i] = *min_element(cs, cs+3) + 1;
	}

	cout << dp[count] << endl;
	return 0;
}
