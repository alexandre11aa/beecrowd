#include <stdio.h>
#include <math.h>

int main() {
    double pi, raio;

    pi = 3.14159;

    scanf("%lf", & raio);

    printf("A=%.4lf\n", (pi * pow(raio, 2)));

    return 0;
}