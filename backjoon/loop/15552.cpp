#include <cstdio>

int main(void) {
	int count, i, a, b;
	scanf("%d", &count);

	for(i=0; i<count; i++) {
		scanf("%d %d", &a, &b);
		printf("%d\n", a+b);
	}

	return 0;
}
