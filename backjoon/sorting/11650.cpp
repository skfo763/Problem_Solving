#include <vector>
#include <utility>
#include <algorithm>
#include <iostream>
using namespace std;

bool compare(const pair<int, int>&a, const pair<int, int>& b) {
	if(a.first == b.first) {
		return a.second < b.second;
	}
	return a.first < b.first;
}

int main(void) {
	
	int i, count;
	vector<pair<int, int>> data;
	scanf("%d", &count);

	for(i=0; i<count; i++) {
		int a, b;
		scanf("%d %d", &a, &b);
		data.push_back(make_pair(a, b));
	}

	sort(data.begin(), data.end(), compare);

	for(i=0; i<count; i++) {
		cout << data[i].first << " " << data[i].second << "\n";
	}

	return 0;
}
