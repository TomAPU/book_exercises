#include <stdio.h>
#include <math.h>

/* p94, 2.32: */
/* Determine whether arguments can be subtracted without overflow */

int tadd_ok( int x , int y )
{
    int sum = x+y;

    if ( (x>0 && y>0 && x+y<0) || (x<0 && x<0 && x+y>0) )
        return 0;
    return 1;
}

/* 当y=Tmin=-pow(2,w-1)时，-y=y
 * 此时，假设x=Tmax=pow(2,w-1)-1, 
 * x-y=pow(2,w-1)-1-(-pow(2,w-1))=pow(2,w)-1=-1, 溢出了;
 * 但是因为此时y=-y, tadd_ok(x,-y)=tadd_ok(x,y)没有溢出，返回为1
 */

/* WARNING: This code is buggy. */
int tsub_ok(int x, int y)
{
    return tadd_ok(x, -y);
}



int main(void)
{
	int x,y, s;

    /* 以下tsub_ok调用全部都返回1 */
	/* case1: negetive overflow */
	x = -pow(2, sizeof(int)*8-1); /* Tmin */
	y = -1;
    
    printf("y=%d, -y=%d\n", y, -y);
    s = x-y;
	printf("(%d)-(%d)=(%d), tsub_ok=%d\n", x, y, s, tsub_ok(x, y) );

	/* case2: -pow(2,w-1)<=x-y<0 */
	x = -pow(2, sizeof(int)*8-1); /* Tmin */
	y = 1;
    s=x-y;
	printf("(%d)-(%d)=(%d), tsub_ok=%d\n", x, y, s, tsub_ok(x, y) );

	/* case3: 0<=x-y<pow(2,w-1) */
	x = pow(2, sizeof(int)*8-1)-1; /* Tmax */
	y = -1;
    s = x + y;
	printf("(%d)-(%d)=(%d), tsub_ok=%d\n", x, y, s, tsub_ok(x, y) );

	/* case4: positive overflow */
	x = pow(2, sizeof(int)*8-1)-1; /* Tmax */
	y = 1;
    s = x + y;
	printf("(%d)-(%d)=(%d), tsub_ok=%d\n", x, y, s, tsub_ok(x, y) );

	/* case4: positive overflow */
	x = pow(2, sizeof(int)*8-1)-1; /* Tmax */
	y = -pow(2, sizeof(int)*8-1); /* Tmin */
    s = x + y;
	printf("(%d)-(%d)=(%d), tsub_ok=%d\n", x, y, s, tsub_ok(x, y) );
}
