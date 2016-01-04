#include <stdio.h>
#include <math.h>

/* Determine whether arguments can be added without overflow */

int tadd_ok( int x , int y )
{
	long long z = (long long)x + (long long )y; /*x,y must cast to long long, or x+y will be in int */
	long long low = -pow(2, sizeof(int)*8-1);
	long long  upp = pow(2, sizeof(int)*8-1);
	printf("low=%lld\n", low);
	printf("upp=%lld\n", upp);
	printf("z=%lld\n", z);

	if ( (z >= low) && (z < upp) )
		return 1;
	else
		return 0;
}

int tadd_ok2(int x, int y)
{
	int sum = x+y;
	printf("sum=%d\n", sum);
	printf("sizeof(sum)=%d\n", sizeof(sum));
	return (sum-x==y) && (sum-y==x);
}

int main(void)
{
	int x,y;
	/* positive overflow */
	printf("sizeof(int)=%d\n", sizeof(int));
	printf("sizeof(long)=%d\n", sizeof(long));
	printf("sizeof(long long)=%d\n", sizeof(long long));
	x = pow(2, sizeof(int)*8-1) - 1;
	y = 1;
	printf("cond 4:\n");
	printf("%d+%d, %d\n",  x, y, tadd_ok2(x, y ) );

	/* ok */
	x = 1;
	y = 1;
	printf("cond 3:\n");
	printf("%d+%d, %d\n",  x, y, tadd_ok2(x, y ) );

	/* ok */
	x = -1;
	y = -1;
	printf("cond 2:\n");
	printf("%d+%d, %d\n", x, y, tadd_ok2(x, y ) );

	/* negetive overflow */
	x = -pow(2, sizeof(int)*8-1);
	y = -1;
	printf("cond 1:\n");
	printf("%d+%d, %d\n", x, y, tadd_ok2(x, y ) );
}
