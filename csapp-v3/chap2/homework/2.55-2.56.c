/*
 * 2.55.
Compile and run the sample code that uses show_bytes (file show-bytes. c) on
different machinys to which you have access. Determine the byte orderings used by these machines.
*/

/*
 * 2.56.
Try running the code for show_bytes for different sample values.
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

void show_int( int x )
{
	show_bytes( (byte_pointer)&x, sizeof(int) );
}

void show_float( float x )
{
	show_bytes( (byte_pointer)&x, sizeof(float));
}

void show_pointer( void *x )
{
	show_bytes( (byte_pointer) &x, sizeof(void *));
}

void test_show_bytes( int val )
{
	int ival = val;
	float fval = (float) ival;
	int *pval = &ival;

	printf("\tAs int: " ) ;
    show_int( ival );
	printf("\tAs float: " ) ;
	show_float( fval );
	printf("\tAs pointer: " ) ;
	show_pointer( pval );
}

int main( int argc, char * argv[] )
{
    printf("Decimal value 12345:\n");
	test_show_bytes( 12345 );

    printf("Hex value 0x12345678:\n");
	test_show_bytes( 0x12345678 );

    printf("Hex value 0x78563412:\n");
	test_show_bytes( 0x78563412 );
}
