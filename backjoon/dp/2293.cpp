#include <stdio.h>
#include <vector>
using namespace std;

#define MAX_COIN_SIZE 101
#define MAX_SUM_SIZE 10001

int coin[MAX_SUM_SIZE];
int dp[10001];

void executeDP(int n, int k, int* coin) {
    for(int i=0; i<n; i++) {
        for(int j=1; j<=k; j++) {
            if(j - coin[i] >= 0) dp[j] += dp[j-coin[i]];
        }
    }
}


int main() {
    int n, k;
    scanf("%d %d", &n, &k);

    for(int i=0; i<n; i++) {
        scanf("%d", &coin[i]);
    }

    dp[0] = 1;

    executeDP(n, k, coin);
    printf("%d", dp[k]);
    return 0;
}
