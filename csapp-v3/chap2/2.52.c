#include <stdio.h>
#include <inttypes.h>

/* p125, 2.52: */
/*  x == (int)(double) x
 *  是否成立？
 */

int32_t int_x_equals_int_double_x()
{
    int32_t x;
    for( x= 0x800

}

int main(void)
{
	int32_t x;

	x = -16;
	printf("x=%" PRId32 ", x/16=%" PRId32 "\n", x, div16(x)); /* -1 */
	x = -17;
	printf("x=%" PRId32 ", x/16=%" PRId32 "\n", x, div16(x)); /* -1.xxx--> -1, 近似值趋向0端 */

	x = 0;
	printf("x=%" PRId32 ", x/16=%" PRId32 "\n", x, div16(x)); /* 0 */

	x = 16;
	printf("x=%" PRId32 ", x/16=%" PRId32 "\n", x, div16(x)); /* 1 */

	x = 17;
	printf("x=%" PRId32 ", x/16=%" PRId32 "\n", x, div16(x)); /* 1.xxx --> 1, 近似值趋向0端 */

}
