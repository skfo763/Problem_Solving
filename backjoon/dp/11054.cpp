#include <iostream>
#include <algorithm>
using namespace std;

int data[1010];
int ldp[1010];
int rdp[1010];
int result[1010];

int main(void) {
	int i, j, count;
	scanf("%d", &count);

	for(i=1; i<=count; i++) {
		scanf("%d", &data[i]);
	}

	ldp[0] = 0; ldp[1] = 1;
	rdp[0] = 0; rdp[count] = 1;

	for(i=2; i<=count; i++) {
		int max = 0;
		for(j=1; j<i; j++) {
			if(data[j] < data[i] && ldp[j] > ldp[max]) {
				max = j;
			}
		}
		ldp[i] = ldp[max] + 1;
	}

	for(i=count-1; i>=1; i--) {
		int min = 0;
		for(j=count; j>i; j--) {
			if(data[j] < data[i] && rdp[j] > rdp[min]) {
				min = j;
			}
		}
		rdp[i] = rdp[min] + 1;
	}

	for(i=1; i<=count; i++) {
		result[i] = ldp[i]+rdp[i];
	}

	cout << *max_element(result, result+count+1)-1 << endl;


	return 0;
}
