#include <iostream>
#include <algorithm>
using namespace std;
int number = 9;
int heap[9] = {7, 6, 5, 8, 3, 5, 9, 1, 6};

int main(void){
	// �� ���� :  �� Ʈ�� ������ �̿��ϴ� ���� ���. >> �׻� O(NlogN)
	// ���� Ʈ��: ��� ����� �ڽ� ��尡 2�� ������ Ʈ������
	// Ʈ���� �ֻ��: ��Ʈ / ���ϴ�: ����
	// ���� ���� Ʈ��: �����Ͱ� ���� �ڽ� ���, ������ �ڽ� ���� �������� ���� ����
	// �� : �ּڰ��̳� �ִ��� ������ ã�Ƴ��� ���� ��������Ʈ���� ������� �ϴ� Ʈ��
	// �ִ� ��: �θ� ��尡 �ڽ� ��庸�� ū ��. 
	// �� ���� �˰��� : Ư���� ����� �� �ڽ� �߿��� �ڱ⺸�� �� ū �ڽİ�
	// 					  �ڽ��� ��ġ�� �ٲٴ� �˰��� >> O(logN)
	// �������� �������İ� �ٸ��� ������ �߰����� �迭�� �ʿ����� �ʴٴ� ������
	// �޸� ���鿡�� ���� ȿ������. 
	
	
	//���� ��ü Ʈ�� ������ �ִ� �� ������ �ٲߴϴ�. 
	for(int i=1; i<number ; i++){
		int c = i;
		do{
			int root = (c-1) /2;
			if(heap[root] < heap[c]){
				int temp = heap[root];
				heap[root] = heap[c];
				heap[c] = temp;
			}
			c = root;
		} while(c != 0);
	}
	//ũ�⸦ �ٿ����� �ݺ������� ���� ����
	for(int i=number-1; i>=0; i--){
		int temp = heap[0];
		heap[0] = heap[i];
		heap[i] = temp;
		int root = 0;
		int c= 1;
		do{
			c = 2*root + 1;
			//�ڽ��߿� �� ū ���� ã��
			if(heap[c] < heap[c+1] && c < i-1){
				c++;
			} 
			//��Ʈ���� �ڽ��� �� ũ�ٸ� ��ȯ
			if(heap[root] < heap[c] && c < i){
				int temp = heap[root];
				heap[root] = heap[c];
				heap[c] = temp;
			} 
			root = c;
		} while(c < i);
	} 
	
	for(int i=0; i<number; i++){
		cout << heap[i] << ' ';
	}
	
	
	return 0;
}
