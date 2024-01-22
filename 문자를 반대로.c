#include <stdio.h>
int main(void) {
	char text[9] = { 'P','A','T','H','L','E','V','E','L'};
	for (int i = 8; i >= 0; i--) {
		printf("%c", text[i]);
	}
}
