#include <stdio.h>
#include <math.h>

int main () {

    double A1, A2, B1, B2, value;
    char line_A[50], line_B[50];

    fgets(line_A, sizeof(line_A), stdin);
    sscanf(line_A, "%lf %lf", &A1, &A2);

    fgets(line_B, sizeof(line_B), stdin);
    sscanf(line_B, "%lf %lf", &B1, &B2);

    value = sqrt(pow((A1 - B1), 2) + pow((A2 - B2), 2));

    printf("%.4lf\n", value);

    return 0;
}