#include <iostream>
using namespace std;

// ���� �� ������谡 ���� ���� ���Ѵ�� ǥ���ϴµ� �̸� INF�� ������. 
#define INF 987654321
// ������ ���� ����. 
#define SIZE 4

// �ִ� ����� �Ÿ��� ǥ���ϴ� �迭 D��, �ִ� ��� ���̿� ���� ������ ǥ���ϴ� �迭 P ����. 
int D[SIZE][SIZE];
int P[SIZE][SIZE];

// �Է� �����͸� ��Ÿ���� �迭 W ���� �� �ʱ�ȭ. 
int W[SIZE][SIZE] = {
	// ���� �Է� ������
	{0,3,INF,8},
	{6,0,7,INF},
	{2,INF,0,5},
	{INF,INF,2,0}
	
	/*
	// ���� �Է� ������
	{0,1,INF,1,5},
	{9,0,3,2,INF},
	{INF,INF,0,4,INF},
	{INF,INF,2,0,3},
	{3,INF,INF,INF,0}*/
};

// �Ű�����: ������ ���� n, �Է� ������ W, ���� �迭 D, ���� �迭 P. 
void floyd2(int n, const int W[][SIZE], int(*D)[SIZE], int(*P)[SIZE]){
	int i, j, k;
	
	// P�迭�� -1�� �ʱ�ȭ, �迭�� �ε���(����)�� 0���� �����ϱ� ����.
	for(i=0; i<n; i++){
		for(j=0; j<n; j++){
			P[i][j] = -1;
		}
	}
	// D�迭�� �ʱⰪ�� W�� ������ �ʱ�ȭ. 
	for(i=0; i<n; i++){
		for(j=0; j<n; j++){
			D[i][j] = W[i][j];
		}
	}
	
	/*
	�ִܰ���� ���̿� �ִܰ�� ������ ���� �ľ�.
	i�� j�� �ִܰ���� ���� D[i][j]���� ���� k�� ���� ���� ��찡 �� ���� ���,
	D[i][j]�� k�� ���� ���� ����� ���� ���� & P[i][j]�� k ����.
	*/
	for(k=0; k<n; k++){
		for(i=0; i<n; i++){
			for(j=0; j<n; j++){
				if(D[i][k] + D[k][j] < D[i][j]){
					P[i][j] = k;
					D[i][j] = D[i][k] + D[k][j];
				}
			}
		}
	}
	
	//D ���  
	printf ("D: �ִܰ���� ����\n"); 
    for (int i = 0; i < n; i++){
        for (int j = 0; j < n; j++){
            if (D[i][j] == INF)
                printf("%7s", "INF");
            else
                printf ("%7d", D[i][j]);
        }
        printf("\n");
    }
    
    //P ��� 
    printf ("P: �ִܰ�� �� ���� ����\n");
    for (int i = 0; i < n; i++){
        for (int j = 0; j < n; j++){
            printf ("%7d", P[i][j]);
        }
        printf("\n");
    }
}

// �Ű�����: ���� q�� ���� r
void path(int q, int r){
	// P�� �ʱⰪ�� -1�� �ʱ�ȭ �߱� ������ -1�� ��
	if(P[q][r] != -1){
		//��͸� ���� �ݺ��Ǵ� ���� �� ����. 
		path(q, P[q][r]);
		cout << " v" << P[q][r];
		path(P[q][r], r);
	}
}

int main(void){
	floyd2(SIZE, W, D, P);
	
	// ����� ����� �̸����� �迭�� ��Ÿ���� path(5,3)������,
	// �� ���α׷������� ������ �̸� 5�� 3�� �迭�δ� 4�� 2�� ǥ���Ǳ� ������,
	// path(5,3) => path(4,2) �� ǥ���Ѵ�. 
	path(3,1);
	
	return 0;
}
