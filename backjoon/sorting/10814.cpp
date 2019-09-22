#include <iostream>
#include <algorithm>
#include <vector>
#include <utility>
using namespace std;

class student {

	public : 
		int age;
		string name;
		int num;
};

bool comp(const student &s1, const student &s2) {
	if(s1.age == s2.age) {
		return s1.num < s2.num;
	}
	return s1.age < s2.age;
}

int main(void) {
	int i, count;
	scanf("%d", &count);
	vector<student> data;

	for(i=0; i<count; i++) {
		student s;
		cin >> s.age >> s.name;
		s.num = i;
		data.push_back(s);
	}

	sort(data.begin(), data.end(), comp);

	for(i=0; i<count; i++) {
		cout << data[i].age << " " << data[i].name << "\n";
	}

	return 0;
}
