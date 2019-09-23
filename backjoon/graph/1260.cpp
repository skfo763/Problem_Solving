#include <iostream>
#include <vector>
#include <algorithm>
#include <stack>
#include <queue>
using namespace std;

class Vertex {
	public:
		vector<int> v;
		bool visited;
};


int main(void) {
	
	int i, j, n, m, st;
	scanf("%d %d %d", &n, &m, &st);
	Vertex graph[n+1];

	for(i=1; i<=n; i++) {
		Vertex v;
		v.visited = false;
		graph[i] = v;
	}

	for(i=0; i<m; i++) {
		int a, b;
		scanf("%d %d", &a, &b);
		graph[a].v.push_back(b);
		graph[b].v.push_back(a);
	}

	stack<int> s;
	s.push(st);
	bool flag;
	cout << st << " ";

	while(!s.empty()) {
		Vertex visit = graph[s.top()];
		graph[s.top()].visited = true;
		flag = false;	
		
		sort(visit.v.begin(), visit.v.end());
		for(i=0; i<visit.v.size(); i++) {
			int pos = visit.v[i];
			
			if(graph[pos].visited == false) {
				s.push(pos);
				cout << pos << " ";
				flag = true;
				break;
			}
		}
		
		if(!flag) {
			s.pop();
		}
	}

	for(i=1; i<=n; i++) {
		graph[i].visited = false;
	}
	
	cout << endl;
	queue<int> q;
	q.push(st);

	while(!q.empty()) {
		Vertex visit = graph[q.front()];
		graph[q.front].visited = true;
		cout << q.front() << " ";
		
		sort(visit.v.begin(), visit.v.end());
		for(i=0; i<visit.v.size(); i++) {
			int pos = visit.v[i];

			if(graph[pos].visited == false) {
				q.push(pos);
			}
		}
		q.pop();
	}

	cout << endl;

	return 0;
}
