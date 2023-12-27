#include <stdio.h>
main() {
		for (int i = 1; i <= 500; i++) {
			int sum = 0;
			for (int j = 1; j < i; j++) {
				if (i % j == 0) {
					sum += j;
				}
			}
			if (sum == i) {
				printf("%d\n", i);
		}
	}
}// 문제 : 다음은 1부터 500까지의 수 중에서 완전수를 구하는 C 언어 프로그램이다. 
// 완전수 : 자신을 제외한 자신의 약수를 모두 더한 값이 자신과 일치하는 수
