#include <stdio.h>
int main() {
	int score[5] = { 90, 85, 60, 95, 50 };
	int rank;

	for (int i = 0; i < 5; i++) {
		rank = i;
		for (int j = 0; j < 5; j++) {
			if (score[i] < score[j]) {
				rank++;
			}
		}
		printf("%d번: %d위\n", i + 1, rank);

	}

}
