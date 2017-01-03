/*
2.58
write a procedure is_little_endian that will return 1 when compiled and run on a little-endian machine, and will return 0 when compiled and run on a big-endian machine. This program should run on any machine, regardless of its word size*/

#include <stdio.h>

int is_little_endian()
{
    int val = 0x1234;
    char *p = (char *) &val;
    /* little-endian: 3412... */
    /* big-endian: 1234... */
    return (char)p[0]==0x34 ? 1:0;
}

int main( int argc, char * argv[] )
{
    if (is_little_endian())
        printf("Little endian\n");
    else
        printf("Big endian\n");
}
