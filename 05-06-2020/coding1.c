//write c program to print hollow inverted full pyramid using star pattern
#include <stdio.h>
int main()
{
    int n;
    scanf(“%d”, &n);
    int i, j;
    for (i = 1; i <= n; i++) {
        for (j = 1; j < i; j++) {
            printf(” “);
        }

        for (j = 1; j <= (n * 2 – (2 * i – 1)); j++) {

            if (i == 1 || j == 1 || j == (n * 2 – (2 * i – 1))) {
                printf(“*”);
            } else {
                printf(” “);
            }
        }
        printf(“\n”);
    }
}
