#include <stdio.h>
#include <string.h>
 
int main() {

    char A[50];
    double B, C;

    scanf("%s", & A);
    scanf("%lf", & B);
    scanf("%lf", & C);

    printf("TOTAL = R$ %.2lf\n", (B + 0.15 * C));
 
    return 0;
}