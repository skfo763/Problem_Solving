#include <stdio.h>
#include <limits.h>
 
using namespace std;
 
int main() {
    int n,r,c;
    int dp[501][501] = {0};
    int dim[501][2] = {0};
 
    scanf("%d", &n);
    for(int i=1; i<=n; ++i) {
        scanf("%d%d", &r, &c);
        dim[i][0] = r;
        dim[i][1] = c;
    }
 
    for(int d=1; d<n; ++d) {    // interval
        for(int i=1; i<=n-d; ++i) {   // start
            int j = i+d;    // end
            int minimum = INT_MAX;
            for(int k=i; k<j; ++k) {    // mid
                int candidate = dp[i][k]+dp[k+1][j]+dim[i][0]*dim[k][1]*dim[j][1];
                if(candidate < minimum) {
                    minimum = candidate;
                }
            }
            dp[i][j] = minimum;
        }
    }
 
    printf("%d\n", dp[1][n]);
 
}
