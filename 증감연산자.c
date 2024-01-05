#include <stdio.h>
int function(int num) {
	++num;
	return num++;
}
int main() {
	int num1 = 5;
	int num2 = 4;
	int result;
	result = function(num1) + num2++;
	printf("%d %d %d", result, num1, num2);
}
