#include <iostream>
#include <stack>
#include <string>
using namespace std;

int main(void) {
	int i, j, count;
	string input;
	scanf("%d", &count);

	for(i=0; i<count; i++) {
		cin >> input;
		stack<int> s;

		for(j=0; j<input.length(); j++) {
			if(input[j] == '(') {
				s.push(input[j]);

			}
			else if(input[j] == ')' && !s.empty()) {
				s.pop();
			} else {
				s.push(input[j]);
				break;
			}
		}

		if(s.empty()) {
			printf("YES\n");
		} else {
			printf("NO\n");
		}
	}

	return 0;
}
