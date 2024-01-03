#include <stdio.h>
void main() {
	int x = 5, y = 5, a;
	a = --x + y++;
	printf("%d %d %d", a, x, y);
}

