/*
 2.57.
Write procedures show_short, show_long, and show_doubie 'that print the byte
representations of C objects of types short, long, and double, respectively. Try these' out on 'several machines.
*/

#include <stdio.h>

typedef unsigned char *byte_pointer;

void show_bytes( byte_pointer start, int len )
{
	int i;
	for( i=0; i<len; i++ )
		printf(" %.2x", start[i]);
	printf( "\n" );
}

void show_short( short x )
{
	show_bytes( (byte_pointer)&x, sizeof(short) );
}

void show_long( long x )
{
	show_bytes( (byte_pointer)&x, sizeof(long) );
}

void show_double( double x )
{
	show_bytes( (byte_pointer)&x, sizeof(double));
}

void test_show_bytes( byte_pointer bytes )
{
	short short_val = *(short *) bytes;
	long long_val = *(long *) bytes;
	double double_val = *(double *) bytes;

	printf("\tAs short: " ) ;
    show_short( short_val );
	printf("\tAs long: " ) ;
	show_long( long_val );
	printf("\tAs double: " ) ;
	show_double( double_val );
}

int main( int argc, char * argv[] )
{
    char val[] = {0x78,0x56, 0x34, 0x12};
    printf("Hex value 0x12345678:\n");
	test_show_bytes( (byte_pointer)val );

    printf("Hex value 0x78563412:\n");
    char val2[] = {0x12, 0x34, 0x56, 0x78};
	test_show_bytes( (byte_pointer)val2);
}
