#include <iostream>
#include <algorithm>
using namespace std;

int main(void) {
	int a, b;
	scanf("%d %d", &a, &b);

	if(a > b) {
		cout << ">";
	} else if(a < b) {
		cout << "<";
	} else {
		cout << "==";
	}

	cout << endl;
	return 0;
}
