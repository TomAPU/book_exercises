#include <stdio.h>
#include <math.h>

/* p99, 2.35: */
/* Determine whether arguments can be multiplied without overflow */
/*证明：
 * 1. x=0时显然成立
 * 2. 设p为x与y二进制补码相乘的结果, 即p=x *<t> y,
 *    q = p/x;
 *    因为 x*y = p + t*pow(2,w), 当t不为0时则有溢出。
 *    又 p=x*q+r, |r|<|x|。
 *    x*y=p+t*pow(2,w)=x*q+r+t*pow(2,w)
 *    要使q=y当且仅当r=t=0
 */

int tmult_ok( int x , int y )
{
    int p = x*y;

    /* Either x is zero, or dividing p by x gives y */
    return !x || p/x == y;
}


int main(void)
{
	int x,y, s;

    /* pow(2, w-1) 溢出 */
	x = -pow(2, sizeof(int)*8-1); /* Tmin */
	y = -1;
    
    s = x*y;
	printf("(%d)*(%d)=(%d), tmult_ok=%d\n", x, y, s, tmult_ok(x, y) );

	/* -pow(2,w) 溢出*/
	x = -pow(2, sizeof(int)*8-1); /* Tmin */
	y = 2;
    s=x*y;
	printf("(%d)*(%d)=(%d), tmult_ok=%d\n", x, y, s, tmult_ok(x, y) );

	/* -pow(2,w-1)+1, 没有溢出*/
	x = pow(2, sizeof(int)*8-1)-1; /* Tmax */
	y = -1;
    s = x * y;
	printf("(%d)*(%d)=(%d), tmult_ok=%d\n", x, y, s, tmult_ok(x, y) );

	/* pow(2,w)-2 溢出*/
	x = pow(2, sizeof(int)*8-1)-1; /* Tmax */
	y = 2;
    s = x * y;
	printf("(%d)*(%d)=(%d), tmult_ok=%d\n", x, y, s, tmult_ok(x, y) );

	/* 溢出 */
	x = pow(2, sizeof(int)*8-1)-1; /* Tmax */
	y = -pow(2, sizeof(int)*8-1); /* Tmin */
    s = x * y;
	printf("(%d)*(%d)=(%d), tmult_ok=%d\n", x, y, s, tmult_ok(x, y) );
}
