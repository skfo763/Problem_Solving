#include <iostream>
#include <algorithm>
using namespace std;

int data[1010];
int dp[1010];

int main(void) {
	int i, j, count;
	scanf("%d", &count);

	for(i=1; i<count+1; i++) {
		scanf("%d", &data[i]);
	}

	dp[0] = 0; dp[1] = data[1];

	for(i=2; i<=count; i++) {
		int max = 0;

		for(j=1; j<i; j++) {
			if(data[j] < data[i]) {
				if(dp[j] > dp[max]) {
					max = j;
				}
			}
		}

		dp[i] = dp[max] + data[i];
	}

	cout << *max_element(dp, dp+count+1);
	
	return 0;
}
