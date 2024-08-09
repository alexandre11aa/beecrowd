#include <stdio.h>
#include <math.h>

int main() {
 
    double A, B, C;
    char line[50];
    double tri, cir, tra, qua, ret;

    fgets(line, sizeof(line), stdin);
    sscanf(line, "%lf %lf %lf", &A, &B, &C);

    tri = A * C / 2.0;
    cir = 3.14159 * pow(C, 2);
    tra = (A + B) * C / 2.0;
    qua = pow(B, 2);
    ret = A * B;

    printf("TRIANGULO: %.3lf\n", tri);
    printf("CIRCULO: %.3lf\n", cir);
    printf("TRAPEZIO: %.3lf\n", tra);
    printf("QUADRADO: %.3lf\n", qua);
    printf("RETANGULO: %.3lf\n", ret);
 
    return 0;
}