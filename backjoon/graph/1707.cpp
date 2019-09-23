#include <vector>
#include <iostream>
#include <algorithm>
#include <queue>
using namespace std;

bool check_Bip(vector<vector<int>> &a) {
	int size = a.size();
	int color[size] = {0,};

	queue<int> q;
	for(int i=0; i<size; i++) {
		if(color[i] != 0) continue;
		q.push(i);

		while(!q.empty()) {
			int qSize = q.size();

			for(int j=0; j<qSize; j++) {
				int curr = q.front();
				q.pop();
				
				int nearCol = 0;
				for(int next : a[curr]) {
					if(color[next] == 0) {
						q.push(next);
					
					} else {
						if(nearCol == 0) nearCol = color[next];
						else if(nearCol != color[next]) return false;
					}
				}

				color[curr] = (nearCol == 0) ? 1 : 3-nearCol;
			}
		}
	}

	return true;
}




int main(void) {
	
	int i, j, count;
	cin >> count;

	for(i=0; i<count; i++) {
		int v, e;
		cin >> v >> e;
		vector<vector<int>> data(v+1);

		for(j=1; j<=e; j++) {
			int a, b;
			scanf("%d %d", &a, &b);
			data[a].push_back(b);
			data[b].push_back(a);
		}

		if(check_Bip(data)) {
			printf("YES\n");
		} else {
			printf("NO\n");
		}
	}

	return 0;
}
