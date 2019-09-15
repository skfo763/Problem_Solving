#include <iostream>
using namespace std;

int main(void) {
	int i, j, t, count, cul;
	string arr;
	scanf("%d", &count);

	for(i=0; i<count; i++) {
		cin >> arr;
		cul = 0;

		for(j=0; j<arr.size(); j++) {
			if(arr[j] == 'O') {
				t = 0;
				do {
					t += 1;
				} while(arr[j-t] == 'O' && j-t >= 0);
				cul += t;
			}
		}
		
		cout << cul << endl;
		arr.clear();
	}

	return 0;
}
