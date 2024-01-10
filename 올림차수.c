#include <stdio.h>
int main(void) {
	int ar[5] = { 44,66,88,22,11 };
	int i, j, temp;
	for (i = 0; i < 5; i++) {
		for (j = 0; j < 5; j++) {
			if (ar[i] < ar[j]) {
				temp = ar[i];
				ar[i] = ar[j];
				ar[j] = temp;

			}
		}
		for (i = 0; i < 5; i++) {
			printf("%d ", ar[i]);
		}
	}
}
