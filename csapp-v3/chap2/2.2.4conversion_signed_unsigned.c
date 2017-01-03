#include <stdio.h>

int main(void)
{
    short int v = -12345;
    unsigned short uv = (unsigned short) v;
    
	printf("v=%d, uv=%u\n", v, uv);

    /* 输出如下，相互转换时，低层的bit pattern不变
    * v=-12345, uv=53191
    * */

    unsigned u = 4294967295u; /* UMax */
    int tu = (int)u;
	printf("u=%u, tu=%d\n", u, tu);
    /* u=4294967295, tu=-1 */
}
