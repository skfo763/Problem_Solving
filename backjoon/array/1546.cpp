#include <iostream>
#include <algorithm>
using namespace std;

int main(void) {
	int count, i, max;
	scanf("%d", &count);
	int arr[count] = {0, };

	for(i=0; i<count; i++) {
		scanf("%d", &arr[i]);	
	}

	max = *max_element(arr, arr+count);
	double result = 0;

	for(i=0; i<count; i++) {
		result += (arr[i]/(double)max)*100;
	}

	cout << result/count << endl;
	
	return 0;
}
