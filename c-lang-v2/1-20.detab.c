#include <stdio.h>

#define N_TAB_COL   2

int main()
{
    int i, c;

    while ((c = getchar()) != EOF ) {
        if (c == '\t') {
            for(i = 0; i < N_TAB_COL; i++){
                putchar(' ');
            }
        }
        else {
            putchar(c);
        }
    }
}
