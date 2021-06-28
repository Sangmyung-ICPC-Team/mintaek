#include <stdio.h>

int main(void){
	int c,n;
	double m[1000], total, a;
	scanf("%d",&c);
	for(int i = 0; i < c; i++){
		total = 0;
		a = 0;
		scanf("%d",&n);
		for(int j = 0; j < n; j++){
			scanf("%lf",&m[j]);
			total += m[j];
			
		}
		for(int k = 0; k < n; k++){
			if(m[k] > total/(double)n)
				a++;
		}
		printf("%.3lf",a/n*100);
	}
	return 0;
}


