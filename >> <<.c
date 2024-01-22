#include <stdio.h>
int main(void) {
	int num1, num2, result;
	num1 = 20;
	num2 = 4;

	result = num1 >> 3 << num2;
	printf("%d", result);
}
