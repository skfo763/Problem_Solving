#include <iostream>
#include <string>
using namespace std;

int main(void) {
	long val;
	int i, a, b, c;
	scanf("%d %d %d", &a, &b, &c);
	val = a*b*c;
	
	string str = to_string(val);
	int arr[10] = {0, };

	for(i=0; i<str.size(); i++) {
		arr[str[i]-'0']++;
	}

	for(i=0; i<10; i++) {
		cout << arr[i] << endl;
	}
	
	return 0;
}
