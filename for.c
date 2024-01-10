#include <stdio.h>
int main(void) {
	int a, b = 10;
	for (a = 0; a < 5; a++) {
		b -= a;
	}
	printf("%d, %d", a, b);
}
