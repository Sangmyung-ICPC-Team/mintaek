#include <stdio.h>

int main(void){
	int t;
	double n[1000], m = 0, total = 0;
	scanf("%d",&t);
	for(int i = 0; i < t; i++){
		scanf("%lf",&n[i]);
		if(n[i] > m) m = n[i];
	}
	for(int i = 0; i < t; i++){
		n[i] = (n[i]/m)*100.0;
		total += n[i];
	}
	printf("%.2lf",total/(double)t);
	return 0;
}
