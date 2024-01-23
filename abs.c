#include <stdio.h>
#include <stdlib.h>
void main() {
	int result;
	result = function(20, -31);
	printf("두 수의 차이는 : ");
	printf("%d", result);
}
int function(int i, int j) {
	int result;
	result = abs(i) - abs(j);
	return result;
}
