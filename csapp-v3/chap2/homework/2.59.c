/*
2.59
Write a C expression that will yield a word consisting of the least significant byte of
x and the temaining bytes of y. For operands x = Ox89ABCDEF and y = Ox76543210,
this would give Ox765432EF. 
 */

#include <stdio.h>

int main( int argc, char * argv[] )
{
    int x = 0x89ABCDEF;
    int y = 0x76543210;
    int z = (x&0xFF)|(y&(~0xFF));
    printf("x=%x, y=%x, z=%x\n", x, y, z);
}
