#include <iostream>
using namespace std;

int main(void) {
	int value, temp, count, a, b;
	scanf("%d", &value);
	count = 0;

	if(value < 10) {
		value *= 10;
	}
	temp = value;


	do {
		a = temp/10;
		b = temp%10;

		temp = (b*10) + ((a+b)%10);
		count++;
	} while(temp != value);
	
	cout << count << endl;
	return 0;
}
