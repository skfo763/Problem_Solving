#include <iostream>

int main(void) {
	int i, n, x, temp;
	scanf("%d %d", &n, &x);

	for(i=0; i<n; ++i) {
		scanf("%d", &temp);
		if(temp < x) {
			printf("%d ", temp);
		}
	}

	return 0;
}
