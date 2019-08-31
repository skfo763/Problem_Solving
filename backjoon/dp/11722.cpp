#include <iostream>
#include <algorithm>
using namespace std;

int data[1010];
int dp[1010];

int main(void) {
	int i, j, count;
	scanf("%d", &count);

	for(i=1; i<=count; i++) {
		scanf("%d", &data[i]);
	}

	dp[0] = 0; dp[count] = 1;

	for(i=count-1; i>=1; i--) {
		int min = 0;

		for(j=count; j>i; j--) {
			if(data[j] < data[i]) {
				if(dp[j] > dp[min]) {
					min = j;
				}
			}
		}
		
		dp[i] = dp[min] + 1;
	}

	cout << *max_element(dp, dp+count+1) << endl;
	
	return 0;
}
