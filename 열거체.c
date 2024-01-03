#include <stdio.h>
void main() {
	enum subject {kuk, mat=5, eng};
	int a, b;

	a = kuk;
	b = eng;
	printf("a = %d\n", a);
	printf("b = %d\n", b);

}

