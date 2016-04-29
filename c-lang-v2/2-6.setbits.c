#include <stdio.h>

/*
Exercise 2-6. Write a function setbits(x,p,n,y) that returns x with the n bits
that begin at position p set to the rightmost n bits of y, leaving the other bits
unchanged.
*/

long setbits(long x, int p, int n, int y)
{
    int mask;
    if ( y == 0 ) {
        mask = (~0 << (p+1) ) | ~(~0 << (p+1-n)); /* 1111111100000111*/
        return x & mask;
    }
    else {
        mask = ~(~0 << (p+1)) & (~0 << (p+1)-n); /* 0000000000001111110000*/
        return x | mask;
    } 
 }

int main()
{
    if ( setbits( 0xFFFF, 3, 3, 0) == 0xFFF1 ) {
        printf("set to 0 ok\n");
    }
    if ( setbits( 0xFFF1, 3, 3, 1 ) == 0xFFFF ) {
        printf("set to 1 ok\n");
    }
}
