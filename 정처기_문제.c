#include <stdio.h>
int main(void) {
	int num1 = 20;
	int num2 = 3;
	while(num1 != 0) {
		num1 /= num2;
		printf("%d", num1);
	}
	return 0;
}
