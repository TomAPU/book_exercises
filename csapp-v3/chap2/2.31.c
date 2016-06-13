#include <stdio.h>
#include <math.h>

/* p94, 2.31: */
/* Determine whether arguments can be subtracted without overflow */

int tadd_ok( int x , int y )
{
    int sum = x+y;
    return (sum-x == y) && (sum-y == x);

}

/* 不管是否溢出， 整数的运算都满足  (x+y)-x = y; (x+y)-y=x, 故都返回1 */
