#include <stdio.h>
#define min1(x,y) x<y ? x:y

int main(void){
	int n,m,min = 80;
	int B=0,W=0;
	char chess[50][50];
	scanf("%d %d", &n, &m);
	for(int i = 0; i < n; i++){
		scanf("%s",&chess[i]);
	}
	for(int i = 0; i+7 < n; i++){
		for(int j = 0; j < m-7; j++){
			B = 0;
			W = 0;
			for(int x = i; x < i+8; x++){
				for(int y = j; y < j+8; y++){
					if((x + y)%2 == 0){
						if(chess[x][y] == 'B')
							W++;
						else
							B++;
					}
					else{
						if(chess[x][y] == 'B')
							B++;
						else
							W++; 
					}
				}
			}
			min = min1(min, B);
			min = min1(min, W);
		}
	}
	printf("%d\n",min);
	
	return 0; 
}




