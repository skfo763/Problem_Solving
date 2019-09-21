#include <iostream>
#include <string.h>
using namespace std;
int dp[4001][4001];

int main(void) {
	char str1[4001], str2[4001];
	scanf("%s %s", str1, str2);
	int i, j, s1, s2;

	s1 = strlen(str2);
	s2 = strlen(str1);
	int max = 0;

	for(i=1; i<=s1; i++) {
		
		for(j=1; j<=s2; j++) {
			
			if(str2[i-1] == str1[j-1]) dp[i][j] = dp[i-1][j-1]+1;
			else {
				dp[i][j] = 0;
			}

			if(dp[i][j] > max) {
				max = dp[i][j];
			}
		}
	}

	cout << max << endl;

	return 0;
}
