#include <stdio.h>
 
int main() {

    int A;
    double B;

    scanf("%d", &A);
    scanf("%lf", &B);

    printf("%.3lf km/l\n", (A / B));
 
    return 0;
    
}