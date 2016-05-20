#include <stdio.h>
#include <math.h>

/* p94, 2.30: */
/* Determine whether arguments can be added without overflow */
/* 二进制补码表示的有符号数相加溢出的判断为：
 * ( x>0 && y>0 && x+y < 0 ) || (x<0 && y<0 && x+y>0)
 */

int tadd_ok( int x , int y )
{
    int s = x + y;

    if ( ( x>0 && y>0 && s<0 ) || ( x<0 && y<0 && s>0 ) )
        return 0;
    return 1;
}

int main(void)
{
	int x,y, s;

	/* case1: negetive overflow */
	x = -pow(2, sizeof(int)*8-1); /* Tmin */
	y = -1;
    s = x+y;
	printf("(%d)+(%d)=(%d), tadd_ok=%d\n", x, y, s, tadd_ok(x, y) );

	/* case2: -pow(2,w-1)<=x+y<0 */
	x = -pow(2, sizeof(int)*8-1); /* Tmin */
	y = 1;
    s=x+y;
	printf("(%d)+(%d)=(%d), tadd_ok=%d\n", x, y, s, tadd_ok(x, y) );

	/* case3: 0<=x+y<pow(2,w-1) */
	x = pow(2, sizeof(int)*8-1)-1; /* Tmax */
	y = -1;
    s = x + y;
	printf("(%d)+(%d)=(%d), tadd_ok=%d\n", x, y, s, tadd_ok(x, y) );

	/* case4: positive overflow */
	x = pow(2, sizeof(int)*8-1)-1; /* Tmax */
	y = 1;
    s = x + y;
	printf("(%d)+(%d)=(%d), tadd_ok=%d\n", x, y, s, tadd_ok(x, y) );
}
