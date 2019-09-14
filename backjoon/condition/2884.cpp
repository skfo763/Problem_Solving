#include <iostream>
using namespace std;

int main(void) {
	int hour, min;
	scanf("%d %d", &hour, &min);

	if(min >= 45) {

	} else {
		if(hour >= 1) {
			hour -= 1;
			min += 60;
		} else {
			hour = 23;
			min += 60;
		}
	}

	cout << hour << " " << min - 45;
	return 0;
}
