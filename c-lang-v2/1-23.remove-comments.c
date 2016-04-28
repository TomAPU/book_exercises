#include <stdio.h>

#define INIT 0
#define IN_QUOTED  1
#define BEGINNING_COMMENT 2
#define IN_COMMENT 3
#define ENDING_COMMENT 4
#define NO_ESCAPING 0
#define ESCAPING 1

/*
 * For test input "xxxx"
 */

int main()
{
    int i, c, state, escape_state, syntax_error;

    state = INIT;
    escape_state = NO_ESCAPING;
    syntax_error = 0;

    while ( (c = getchar()) != EOF ) {
        if ( syntax_error ) {
            putchar( c );
            continue;
        }

        switch( c ) {
            case '\\':
                switch ( state ) {
                    case IN_COMMENT:
                        escape_state = NO_ESCAPING;
                        break;
                    case BEGINNING_COMMENT:
                        syntax_error = 10;
                        printf("\n===>[error=%d]<===\n", syntax_error);
                        break;
                    case ENDING_COMMENT:
                        syntax_error = 11;
                        printf("\n===>[error=%d]<===\n", syntax_error);
                        break;
                    case INIT :
                    case IN_QUOTED:
                        if ( escape_state == NO_ESCAPING ) {
                            escape_state = ESCAPING;
                            putchar ( c );
                        }
                        else {
                            escape_state = NO_ESCAPING;
                            putchar ( c );
                        }
                        break;
                    default:
                        break;
                }
                break;
            case '"':
                switch ( state ) {
                    case IN_COMMENT:
                        break;
                    case BEGINNING_COMMENT:
                        syntax_error = 20;
                        printf("\n===>[error=%d]<===\n", syntax_error);
                        break;
                    case ENDING_COMMENT:
                        syntax_error = 21;
                        printf("\n===>[error=%d]<===\n", syntax_error);
                        break;
                    case INIT :
                        if ( escape_state == NO_ESCAPING ) {
                            state = IN_QUOTED;
                            putchar ( c );
                        }
                        else {
                            putchar ( c );
                        }
                        break;
                    case IN_QUOTED:
                        if ( escape_state == NO_ESCAPING ) {
                            state = INIT;
                            putchar ( c );
                        }
                        else {
                            putchar ( c );
                        }
                        break;
                    default:
                        break;
                }
                escape_state = NO_ESCAPING;
                break;
            case '/':
                switch ( state ) {
                    case IN_QUOTED:
                        putchar ( c );
                        break;
                    case IN_COMMENT:
                        break;
                    case BEGINNING_COMMENT:
                        syntax_error = 30;
                        printf("\n===>[error=%d]<===\n", syntax_error);
                        break;
                    case ENDING_COMMENT:
                        state = INIT;
                        break;
                    case INIT :
                        if ( escape_state == NO_ESCAPING ) {
                            state = BEGINNING_COMMENT;
                        }
                        else {
                            putchar ( c );
                        }
                        break;
                    default:
                        break;
                }
                escape_state = NO_ESCAPING;
                break;
            case '*':
                switch ( state ) {
                    case IN_QUOTED:
                        putchar ( c );
                        break;
                    case IN_COMMENT:
                        state = ENDING_COMMENT;
                        break;
                    case BEGINNING_COMMENT:
                        state = IN_COMMENT;
                        break;
                    case ENDING_COMMENT:
                        state = ENDING_COMMENT;
                        break;
                    case INIT :
                    default:
                        break;
                }
                escape_state = NO_ESCAPING;
                break;
            default:
                switch ( state ) {
                    case ENDING_COMMENT:
                        state = IN_COMMENT;
                        break;
                    case IN_COMMENT:
                        break;
                    case IN_QUOTED:
                        putchar( c );
                        break;
                    default:
                        putchar( c );
                        escape_state = NO_ESCAPING;
                        state = INIT;
                        break;
                }
                break;
        }
    }
}
