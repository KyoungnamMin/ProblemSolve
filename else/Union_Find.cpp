//���Ͽ� ���ε� : �׷��� �˰��� / ������ ã��
//�������� ��尡 ������ �� �ΰ��� ��带 �����ؼ�,
//���� �� �γ�尡 ���� ���� �׷����� ���ϴ� �� �Ǻ��ϴ� �˰���
#include <iostream>
using namespace std;

//�θ� ��带 ã�� �Լ� 
int getParent(int parent[], int x){
	if(parent[x] == x) return x;
	return parent[x] = getParent(parent,parent[x]);
}

//�� �θ� ��带 ��ġ�� �Լ�
int unionParent(int parent[], int a, int b){
	a = getParent(parent, a);
	b = getParent(parent, b);
	if(a < b) parent[b] = a;
	else parent[a] = b;
} 

// ���� �θ� ������ �� Ȯ��
int findParent(int parent[], int a, int b){
	a = getParent(parent, a);
	b = getParent(parent, b);
	if(a == b) return 1;
	else return 0;
} 
int main(void){
	int parent[11];
	for(int i=1; i<=10; i++){
		parent[i] = i;
	}
	unionParent(parent, 1, 2);
	unionParent(parent, 2, 3);
	unionParent(parent, 3, 4);
	
	unionParent(parent, 5, 6);
	unionParent(parent, 6, 7);
	unionParent(parent, 7, 8);
	cout << "1�� 5�� ����Ǿ� �ֳ���? " << findParent(parent, 1, 5) << "\n";
	//�� ó�� �����ص� 1��5�� ���� �� >> ���� �ٸ� �׷����� ������ �����ϸ� �����. 
	//unionParent(parent, 2, 5);
	//unionParent(parent, 2, 4);
	unionParent(parent, 1, 5);
	cout << "1�� 5�� ����Ǿ� �ֳ���? " << findParent(parent, 1, 5) << "\n";
	
	return 0;
}

