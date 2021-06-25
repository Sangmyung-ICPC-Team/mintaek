#include <stdio.h>
void fibonacci(int n) {
	int ze = 0, on = 1, re = 0;
	for(int i = 0; i <= n; i++){
		ze = on;
		on = re;
		re = ze + on;
	}
	printf("%d %d\n",ze, on);
}
int main(void){
	int t ,n;
	scanf("%d",&t);
	for(int i = 0; i < t; i++){
		scanf("%d",&n);
		fibonacci(n);
	}
	return 0;
}
