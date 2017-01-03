/* p57
 * Using only bit-level and logical operations, write a C expression that is equivalent
to x == y. In other words, it will return 1 when x and y are equal and 0 otherwise.
*/

#include <stdio.h>

int equals(int x, int y)
{
    return !(x^y);
}

int main()
{
    int x,y;
    for(x=0;x<10;x++){
        for(y=0;y<10;y++){
            printf("%d==%d returns:%d\n", x,y,equals(x,y));
        }
    }
    
}
