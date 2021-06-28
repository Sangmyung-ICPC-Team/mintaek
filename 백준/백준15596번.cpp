#include <stdio.h>
long long sum(int n){
	int sum = 0;
	for(int i = 1; i <= n; i++)
		sum += i;
	return sum;
}
int main(){
	int n;
	scanf("%d",&n);
	printf("%d",sum(n));
}
