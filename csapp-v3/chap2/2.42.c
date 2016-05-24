#include <stdio.h>
#include <inttypes.h>

/* p107, 2.42: */
/* Write a function div16 that returns the value x/16 for integer argument x.
 * Your function should not use division, modulus, multiplication, any conditionals (if or ?:),
 * any comparison operators (e.g.,<,>, or==), or any loops.
 * You may assume that data type int is 32 bits long 
 * and uses a two's-complement representation,
 * and that right shifts are performed arithmetically. */

/* 对于整数x除以pow(2,k), 是算术右移实现
 * 1. 当x>0时，值为 x>>k, 
 * 2. 当x<0时，值为 (x + 1<<k -1) >> k
 */

int32_t div16( int32_t x )
{
    /* 先根据最高位计算出偏移量 1<<k-1, 这里k=4 */
    int sign = (x >> 31) & 0x01; /* 负数时为1, 正数时为0 */
    return (x + (sign << 4) - sign) >> 4;
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
