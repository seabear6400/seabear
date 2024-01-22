#include <stdio.h>
int main(void) {
	int num1, num2;
	num1 = 7;
	num2 = 3;

	num1 < num2 ? ++num1 : num2--;

	printf("%d , %d", num1, num2);

}
