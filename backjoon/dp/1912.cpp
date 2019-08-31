#include <iostream>
#include <algorithm>
using namespace std;

int data[100002];
int dp[100002];

int main(void) {
	int i, j, count;
	scanf("%d", &count);

	for(i=1; i<=count; i++) {
		scanf("%d", &data[i]);
	}

	dp[1] = data[1];

	for(i=2; i<=count; i++) {
		int val = dp[i-1] + data[i];
		dp[i] = val < data[i] ? data[i] : val; 
	}

	cout << *max_element(dp+1, dp+count+1);

	return 0;
}
