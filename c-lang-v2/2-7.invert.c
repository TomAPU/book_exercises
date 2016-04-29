#include <stdio.h>

/*
Exercise 2-7. Write a function invert(x,p,n) that returns x with the n bits that
begin at position p inverted (i.e., 1 changed into 0 and vice versa), leaving the
others unchanged.
*/

long invert(long x, int p, int n)
{
    int mask;
    mask = ~(~0 << (p+1)) & (~0 << (p+1)-n); /* 0000000000001111110000*/
    return x ^ mask;
 }

int main()
{
    if ( invert( 0xFFFF, 3, 3) == 0xFFF1 ) {
        printf("invert1 passed!\n");
    }
    if ( invert( 0xFFF1, 3, 3) == 0xFFFF ) {
        printf("invert2 passed!\n");
    }
}
