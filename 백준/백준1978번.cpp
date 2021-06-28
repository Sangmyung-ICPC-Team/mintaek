#include <stdio.h>
int main(void){
	int n, b, cnt = 0;
	int a;
	scanf("%d",&n);
	int i;
	while(n--){
		scanf("%d",&a);
		for(i = 2; i < a; i++){
			if(a%i == 0)
				break;				
		}
		if(i == a)
			cnt++;	
	}
	printf("%d\n",cnt);
	
	return 0;
}
