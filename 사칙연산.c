#include <stdio.h>
int main(void) {
	int a = 45, b=3, c = 3, d = 2;
	a /= b -- + c * d;
	printf("%d", a);
}
