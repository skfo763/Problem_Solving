#include <iostream>

int main(void) {
	int a, i, j, k, d;
	scanf("%d", &a);
	
	for(i=1; i<=a; i++) {
		int count = 2*i-1;
		for(k=0; k<a-i; k++) {
			printf(" ");
		}

		for(j=1; j<=count; j++) {
			if(i==a) {
				printf("*");
			} else {
				if(j==1 || j==count) {
					printf("*");
				} else {
					printf(" ");
				}
			}
		}

		printf("\n");
	}
	
	return 0;
}
