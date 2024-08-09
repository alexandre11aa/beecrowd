#include <stdio.h>
#include <math.h>

int main() {
 
    int A;
    double value;

    scanf("%d", &A);

    value = (4.0 / 3.0) * 3.14159 * pow(A, 3);

    printf("VOLUME = %.3lf\n", value);
 
    return 0;
}