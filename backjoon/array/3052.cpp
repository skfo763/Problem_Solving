#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

int main(void) {
	int arr[10];
	vector<int> res;
	int i, j, a;
	
	for(i=0; i<10; i++) {
		scanf("%d", &arr[i]);
	}

	for(i=0; i<10; i++) {
		res.push_back(arr[i]%42);
	}

	sort(res.begin(), res.end());
	res.erase(unique(res.begin(), res.end()), res.end());
	cout << res.size();
	return 0;
}
