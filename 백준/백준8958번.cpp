#include <stdio.h>
#include <string.h>

int main(void){
	int t, total, a;
	char n[80];
	scanf("%d", &t);
	for(int i = 0; i < t; i++){
		total = 0, a = 1;
		scanf("%s",n);
		for(int j = 0; j < strlen(n); j++){
			if(n[j] == 'O'){
				total += a;
				a++;
			}
			else 
				a = 1;
		}
		printf("%d\n", total);
	} 
	
	return 0;
}
