#include <iostream>
using namespace std;

 int main() {
	cin.tie(NULL);
	ios_base::sync_with_stdio(false);

	int arr[8];
	int count = 0;

	for (int i = 0; i < 8; i++) {
		cin >> arr[i];
		if (i > 0)
			if (arr[i] == arr[i - 1] + 1) count++;
			else if (arr[i] == arr[i - 1] - 1) count--;
	}

	if (count == 7) cout << "ascending" << "\n";
	else if (count == -7) cout << "descending" << "\n";
	else cout << "mixed" << "\n";
	return 0;
}
