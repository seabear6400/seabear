#include <stdio.h>
int function(int num);
void main() {
	int num = 5;
	num = function(num);
	num++;
	printf("%d", num);
}
int function(int num) {
	++num;
	return num++;
}
