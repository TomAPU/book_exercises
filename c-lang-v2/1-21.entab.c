#include <stdio.h>

#define N_TAB_COL  2

int main()
{
    int i, c, num_blanks;

    num_blanks = 0;

    while ((c = getchar()) != EOF ) {
        if (c == ' ') {
            ++num_blanks;
            if (num_blanks >= N_TAB_COL){
                putchar('\t');
                num_blanks -= N_TAB_COL;
            }
        }
        else{
            if (num_blanks > 0){
                for(i = 0; i < num_blanks; i++ ){
                    putchar(' ');
                }
                num_blanks = 0;
            }
            putchar(c);
        }
    }
}
