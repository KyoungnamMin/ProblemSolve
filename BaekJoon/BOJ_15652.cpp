#include <iostream>
#include <vector>
#include <algorithm>
#include <cmath>
using namespace std;

int n, m;
int soo[9] = {0, };

void dfs(int cnt){
	if(cnt==m){
		for(int i=0; i<m; i++){
			cout << soo[i] <<' ';
		}
		cout << "\n";
		return;
	}
	int i = (cnt==0) ? 1:soo[cnt-1];
	for( ; i<=n; i++){
		soo[cnt] = i;
		dfs(cnt+1);
	}
}

int main(void){
	cin >> n >> m;
	dfs(0);
	
	return 0;
}
