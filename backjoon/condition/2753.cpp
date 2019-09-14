#include <iostream>
using namespace std;

int main(void) {
	int val;
	scanf("%d", &val);

	if((val%4 == 0 && val%100 != 0) || val%400 == 0) {
		cout << 1 << endl;
	} else {
		cout << 0 << endl;
	}

	return 0;
}
