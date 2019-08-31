#include <iostream>
#include <algorithm>
using namespace std;

int dp[31][31];
int data[10000][3];

int main(void) {
	int s, i, j, k, count;
	scanf("%d", &count);

	for(i=1; i<=count; i++) {
		for(j=1; j<=2; j++) {
			scanf("%d", &data[i][j]);
		}
	}

	for(s=1; s<=count; s++) {
		dp[1][1] = 1;
		dp[0][0] = 0;

		for(i=1; i<=data[s][1]; i++) {
			for(j=1; j<=data[s][2]; j++) {
				if(i == 1 && j != 1) {
					dp[i][j] = j;
					continue;
				}

				if(j == 1 && i != 1) {
					dp[i][j] = 0;
					continue;
				}

				for(k=1; k<j; k++) {
					dp[i][j] += dp[i-1][j-k];
				}
			}
		}

		cout << dp[data[s][1]][data[s][2]] << endl;
		
		for(i=1; i<=30; i++) {
			for(j=1; j<=30; j++) {
				dp[i][j] = 0;
			}
		}
	}

	return 0;
}
