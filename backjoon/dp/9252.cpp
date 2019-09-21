#include <iostream>
#include <algorithm>
#include <string.h>

using namespace std;
int dp[1001][1001];

int main(void) {
	char str1[1001], str2[1001];
	scanf("%s %s", str1, str2);
	int i, j, s1, s2;

	s1 = strlen(str1);
	s2 = strlen(str2);

	for(i=1; i<=s1; i++) {

		for(j=1; j<=s2; j++) {
			int temp = 0;
			if(str1[i-1] == str2[j-1]) temp = dp[i-1][j-1] + 1;
			dp[i][j] = max(temp, max(dp[i-1][j], dp[i][j-1]));
		}
	}

	

	cout << dp[s1][s2] << endl;

	string result;
    i = s1;
    j = s2;
    while (i>0 && j>0) {

        if(dp[i][j-1] == dp[i-1][j] && dp[i-1][j] == dp[i-1][j-1] && dp[i][j-1] == dp[i-1][j-1] && dp[i-1][j-1] == dp[i][j]-1) {

            result += str1[i-1];
            i--;
            j--;
        } else {

            if(dp[i-1][j] == dp[i][j]) {
                i--;
            } else if(dp[i][j-1] == dp[i][j]) {
                j--;
            }
        }
    }

    reverse(result.begin(), result.end());
    cout << result << endl;

	return 0;
}
