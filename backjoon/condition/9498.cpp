#include <iostream>
using namespace std;

int main(void) {
	int val;
	scanf("%d", &val);

	if(90 <= val && val <= 100) {
		cout << "A" << endl;
		return 0;
	} else if(80 <= val && val < 90) {
		cout << "B" << endl;
		return 0;
	} else if(70 <= val && val < 80) {
		cout << "C" << endl;
		return 0;
	} else if(60 <= val && val < 70) {
		cout << "D" << endl;
		return 0;
	} else {
		cout << "F" << endl;
		return 0;
	}

	return 0;
}
