#include <stdio.h>

/* 
 * "0x123ABC" ==> unsigned long int
 */
 unsigned long htoi(const char h[], int len)
 {
     int i;
     unsigned long ret = 0;
     if ( len > 2 && h[0]=='0' && ( h[1] == 'x' || h[1] == 'X' ) ) {
         for ( i=2; i<len; i++ ) {
             if ( h[i] >= '0' && h[i] <= '9' ){
                 ret = ret*16 + h[i]-'0';
             }
             else if ( h[i] >= 'a' && h[i] <= 'f' ){
                 ret = ret*16 + h[i]-'a'+10;
             }
             else if ( h[i] >= 'A' && h[i] <= 'F' ){
                 ret = ret*16 + h[i]-'A'+10;
             }
         }
     }
     return ret;
 }

int main()
{
    if ( htoi("0x123ABC", 8) == 0x123ABC ) {
        printf("0x123ABC ok\n");
    }
    if ( htoi("0x123aBC", 8) == 0x123ABC ) {
        printf("0x123aBC ok\n");
    }
    if ( htoi("0X123aBC", 8) == 0x123ABC ) {
        printf("0X123aBC ok\n");
    }
}
