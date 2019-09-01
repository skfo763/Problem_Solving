#include <iostream>
#include <algorithm>
#include <utility>
using namespace std;

pair<int, int> data[501];
int dp[502];

bool cmp(pair<int, int>a, pair<int,int> b) {
	return a.first < b.first;
}

int main(void) {
	int i, j, val;
	scanf("%d", &val);

	for(i=1; i<=val; i++) {
		int a, b;
		scanf("%d %d", &a, &b);
		data[i] = make_pair(a, b);
	}

	sort(data, data+val+1, cmp);

	dp[0] = 0;
	for(i=1; i<=val; i++) {
		int max = 0;

		for(j=1; j<i; j++) {
			if(data[j].second < data[i].second) {
				if(dp[j] > dp[max]) {
					max = j;
				}
			}
		}

		dp[i] = dp[max] + 1;
	}

	cout << val - *max_element(dp, dp+val+1) << endl;
	return 0;
}
