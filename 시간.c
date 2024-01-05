#include <stdio.h>
int main() {
	int num, hour,minute;
	printf("minute : ");
	scanf_s("%d", &num);
	if (num >= 60) {
		hour = num / 60;
		minute = num % 60;
		printf("%d시간 %d분이다.", hour, minute);
	}
	else {
		printf("%d분이다.\n", num);
	}
}
