#include <stdio.h>

int main () {

    double A1, A2, A3, B1, B2, B3, value;
    char line_A[50], line_B[50];

    fgets(line_A, sizeof(line_A), stdin);
    sscanf(line_A, "%lf %lf %lf", &A1, &A2, &A3);

    fgets(line_B, sizeof(line_B), stdin);
    sscanf(line_B, "%lf %lf %lf", &B1, &B2, &B3);

    value = A2 * A3 + B2 * B3;

    printf("VALOR A PAGAR: R$ %.2lf\n", value);

    return 0;
}