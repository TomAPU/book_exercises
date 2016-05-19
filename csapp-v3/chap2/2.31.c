#include <stdio.h>
#include <math.h>

/* p94, 2.31: */
/* Determine whether arguments can be added without overflow */
/* WARNING: This code is buggy. */

/*　(sum-x==y) && (sum-y==x)是永远成立的，
 *  例如，对于 sum-x, 不管sum溢出与否，值都会最终等于y
 *  例： x= Tmin=-pow(2,w-1), y= -1, 此时x+y会溢出。
 *  sum = x+y　溢出后最终值为　-pow(2,w-1)-1+pow(2,w)=pow(2,w-1)-1
 *  对于(sum-x==y)的判断：
 *  sum-x=pow(2,w-1)-1-(-pow(2,w-1))=pow(2,w)-1, 溢出后最终sum=pow(2,w)-1-pow(2,w)=-1, 即(sum-x==y) 类似 (sum-y==x)也永远成立*/

int tadd_ok( int x , int y )
{
    int sum = x + y;

    return (sum-x==y) && (sum-y == x);
}

int main(void)
{
	int x,y, s;

    /* 以下tadd_ok调用全部都返回1 */
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
