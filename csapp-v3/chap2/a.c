#include <stdio.h>

int main(void)
{
	int f;
	int left = -2147483647-1U ;
	f = left < 2147483647;
	printf("left=%d=%u  f=%d\n", left, left, f);
}
