#include <cstdio>
#include <string.h>
#include <algorithm>
 
using namespace std;
 
int main()
{
    char arr[5003] = {' ', };
    int dp[5003] = { 0, };
    int i;
 
    scanf("%s", arr + 1);
    if (arr[1] == '0') {
        printf("0");
        return 0;
    }
 
    dp[0] = dp[1] = 1;
    for (i = 2; i < strlen(arr); i++) {
        if (arr[i] != '0')
            dp[i] = dp[i - 1] % 1000000;
 
        if (arr[i - 1] == '1' || arr[i - 1] == '2' && arr[i] <= '6')
            dp[i] += dp[i - 2] % 1000000;
    }
 
    printf("%d", dp[strlen(arr) - 1] % 1000000);
 
}

