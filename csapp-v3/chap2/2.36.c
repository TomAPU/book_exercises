#include <stdio.h>
#include <math.h>
#include <inttypes.h> /* 头文件不是书上说的 <stdint.h> */

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

int tmult_ok( int32_t x , int32_t y )
{
    int32_t p = x*y;

    /* Either x is zero, or dividing p by x gives y */
    return !x || p/x == y;
}

/* p99, 2.36: */
/* 对于32位的整数，用64位的整数的结果来判断是否有溢出，实现不用2.35题中除法的方法 */

int tmult_ok2( int32_t x , int32_t y )
{
    int64_t p = (int64_t)x * y; /*一定要先将右边手动转成 int64_t */
    /*printf("p=%" PRId64 ", q=%" PRId32 "\n", p,q);*/

    return p == (int32_t) p;
}


int main(void)
{
	int x,y, s;

    /* pow(2, w-1) 溢出 */
	x = -pow(2, sizeof(int)*8-1); /* Tmin */
	y = -1;
    
    s = x*y;
	printf("(%d)*(%d)=(%d), tmult_ok=%d\n", x, y, s, tmult_ok(x, y) );
	printf("(%d)*(%d)=(%d), tmult_ok2=%d\n", x, y, s, tmult_ok2(x, y) );

	/* -pow(2,w) 溢出*/
	x = -pow(2, sizeof(int)*8-1); /* Tmin */
	y = 2;
    s=x*y;
	printf("(%d)*(%d)=(%d), tmult_ok=%d\n", x, y, s, tmult_ok(x, y) );
	printf("(%d)*(%d)=(%d), tmult_ok2=%d\n", x, y, s, tmult_ok2(x, y) );

	/* -pow(2,w-1)+1, 没有溢出*/
	x = pow(2, sizeof(int)*8-1)-1; /* Tmax */
	y = -1;
    s = x * y;
	printf("(%d)*(%d)=(%d), tmult_ok=%d\n", x, y, s, tmult_ok(x, y) );
	printf("(%d)*(%d)=(%d), tmult_ok2=%d\n", x, y, s, tmult_ok2(x, y) );

	/* pow(2,w)-2 溢出*/
	x = pow(2, sizeof(int)*8-1)-1; /* Tmax */
	y = 2;
    s = x * y;
	printf("(%d)*(%d)=(%d), tmult_ok=%d\n", x, y, s, tmult_ok(x, y) );
	printf("(%d)*(%d)=(%d), tmult_ok2=%d\n", x, y, s, tmult_ok2(x, y) );

	/* 溢出 */
	x = pow(2, sizeof(int)*8-1)-1; /* Tmax */
	y = -pow(2, sizeof(int)*8-1); /* Tmin */
    s = x * y;
	printf("(%d)*(%d)=(%d), tmult_ok=%d\n", x, y, s, tmult_ok(x, y) );
	printf("(%d)*(%d)=(%d), tmult_ok2=%d\n", x, y, s, tmult_ok2(x, y) );
}
