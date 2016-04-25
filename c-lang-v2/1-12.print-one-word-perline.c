#include <stdio.h>

#define LN_PRINTED 1
#define LN_NOT_PRINTED 0

int main()
{
    int state, c;

    state = LN_PRINTED;
    while ((c = getchar()) != EOF ) {
        if (c == ' ' || c == '\n' || c == '\t') {
            if (state == LN_NOT_PRINTED) {
                putchar('\n');
                state = LN_PRINTED;
            }
        }
        else {
            putchar(c);
            if (state == LN_PRINTED) {
                state = LN_NOT_PRINTED;
            }
        }
    }
}
