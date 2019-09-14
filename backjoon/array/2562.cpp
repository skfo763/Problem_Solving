#include <iostream>
#include <algorithm>
#include <vector>
using namespace std;

bool cmp(const pair<int,int>& a, const pair<int,int>& b) {
	return a > b;
}

int main(void) {
	vector< pair<int,int> > a;
	int temp;

	for(int i=0; i<9; i++) {
		scanf("%d", &temp);
		a.push_back(make_pair(temp, i+1)); 
	}

	sort(a.begin(), a.end(), cmp);
	cout << a[0].first << endl << a[0].second << endl;
}
