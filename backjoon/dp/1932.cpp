#include <iostream>
#include <algorithm>
#include <utility>
using namespace std;

int dt[502][502];
int dp[502][502];

int main(void) {
	int i, j, count, val;
	scanf("%d", &count);
	
	for(i=1; i<=count; i++) {
		for(j=1; j<=i; j++) {
			scanf("%d", &dt[i][j]);
		}
	}

	dp[1][1] = dt[1][1];
	for(i=2; i<=count; i++) {
		for(j=1; j<=i; j++) {
			if(j == 1) {
				dp[i][j] = dp[i-1][j] + dt[i][j];
				continue;
			}

			if(j == i) {
				dp[i][j] = dp[i-1][j-1] + dt[i][j];	
				continue;
			}
			
			dp[i][j] = max(dp[i-1][j], dp[i-1][j-1]) + dt[i][j];
		}
	}

	for(i=1; i<=count; i++) {
		for(j=1; j<=i; j++) {
			cout << dp[i][j] << " ";
		}
		cout << endl;
	}
	
	if(count == 1) {
		cout << dp[1][1] << endl;
	} else {
		cout << *max_element(dp[count], dp[count]+count+1) << endl;
	}

	return 0;
}

