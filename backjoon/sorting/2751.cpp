#include <cstdio>
using namespace std;
int bucket[2000002] = {0, };

int main(void) {
	int count, i;
	scanf("%d", &count);

	for(i=0; i<count; i++) {
		int a;
		scanf("%d", &a);
		a += 1000000;
		bucket[a]++;
	}

	for(i=0; i<=2000000; i++) {
		if(bucket[i] != 0) {
			printf("%d\n", i-1000000);
		}
	}
}

