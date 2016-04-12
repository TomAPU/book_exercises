#include <stdio.h>

/* Declarations of functions implementing operations bis and bic */
int bis(int x, int m)
{
    return x | m;
}

int bic(int x, int m)
{
    return x & (~m);
}

/* Computer x|y using only calls to functions bis and bic */
int bool_or(int x, int y)
{
    int result = bis(x, y);
    return result;
}

/* Computer x^y using only calls functions bis and bic */
int bool_xor(int x, int y)
{
    int result = bis( bic(x,y), bic(y,x) );
    return result;
}

int main()
{
    int x, y;
    for(x=100,y=200; x<=200; x+=10,y+=10){
        if (bool_or(x, y) == (x|y))
            continue;
        else
            printf("bool_or(%d,%d)=%d, %d|%d=%d\n", x,y,bool_or(x,y), x, y, (x|y));

        if (bool_xor(x, y) == (x^y))
            continue;
        else
            printf("bool_xor(%d,%d)=%d, %d^%d=%d\n", x,y,bool_xor(x,y), x, y, (x^y));
    }
}
