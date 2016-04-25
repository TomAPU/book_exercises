#include <stdio.h>

#define INIT 0
#define IN_QUOTED  1
#define IN_COMMENT 2
#define BEGINNING_COMMENT 3
#define IN_COMMENT 4
#define ENDING_COMMENT 5

int main()
{
    int i, c, state;

    state = INIT;

    while ((c = getchar()) != EOF ) {
        if ( c == '"') {
        }
        else if ( c == '/' ) {

        }
        else if ( c == '*' ) {

        }
    }
}
