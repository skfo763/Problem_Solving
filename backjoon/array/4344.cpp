#include <iostream>
#include <algorithm>
using namespace std;

int main(void) {
	int i, j, count, num;
	float mean;
	scanf("%d", &count);

	for(i=0; i<count; i++) {
		scanf("%d", &num);
		int *arr = new int [num];
		int res = 0;
		mean = 0;

		for(j=0; j<num; j++) {
			scanf("%d", &arr[j]);
			mean += (float) arr[j];
		}		
		mean /= (float) num;

		for(j=0; j<num; j++) {
			if(arr[j] > mean) res += 1;
		}

		printf("%0.3f%\n", ((float)res/num * 100));
		delete [] arr;
	}

	return 0;
}
