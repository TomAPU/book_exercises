/* WARNING: This is buggy code */

float sum_elements( float a[], unsigned length )
/*fix: float sum_elements( float a[], int length )*/
{
	int i;
	float res = 0;

	for (i=0; i<= length-1; i++)
		res += a[i];
	return res;
}

int main( void )
{
	float b[] = {1,2,3};
	return sum_elements( b, 0 );
}
