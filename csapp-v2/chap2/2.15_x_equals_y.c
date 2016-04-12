#include <stdio.h>

int equals(int x, int y)
{
    int z = x^y;
    return !z;
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
