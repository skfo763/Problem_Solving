#include <iostream>
#include <algorithm>
using namespace std;
int dp[1001][1001];

int main(void) {
	char val1[1001], val2[1001];
	scanf("%s %s", val1+1, val2+1);
	int i, j, temp;

	for(i=1; val1[i]; i++) {
		for(j=1; val2[j]; j++) {
			if(val1[i] == val2[j]) temp = 1;
			else temp = 0;
			dp[i][j] = max(dp[i-1][j-1]+temp, max(dp[i][j-1], dp[i-1][j]));
		}
	}

	cout << dp[i-1][j-1];
	return 0;
}
