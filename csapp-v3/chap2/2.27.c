#include <stdio.h>
#include <math.h>

/* p27
 * 2.27:
 * Determine whether arguments can be added without overflow 
 *
 * 对于无符号数x,y, s=x+y 
 * 没有溢出时 s>=x
 * 溢出时，s=x+y-pow(2,w), 由于 y的区间是[0, pow(2,w)-1], y<pow(2,w)
 * 故 s=x+y-pow(2,w) < x
 */

int uadd_ok(unsigned x, unsigned y)
{
    unsigned s = x+y;

    return s < x ? 0: 1;
}

int main(void)
{
	unsigned x,y;

	/* add ok */
    x = 1;
    y = 2;
	printf("%u + %u = %u, uadd_ok=%d\n", x, y, x+y, uadd_ok(x,y) );

    /*
	 overflow 
    */
    x = 1;
    /*y = pow(2, size)-1;*/
    y = (unsigned)(pow(2, sizeof(unsigned)*8) - 1);
	printf("%u + %u = %u, uadd_ok=%d\n", x, y, x+y, uadd_ok(x,y) );
}
