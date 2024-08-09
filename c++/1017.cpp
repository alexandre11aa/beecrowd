#include <stdio.h>
 
int main() {

    int A, B;
    double value;

    scanf("%d", &A);
    scanf("%d", &B);

    value = A * B / 12.0;

    printf("%.3lf\n", value);
 
    return 0;
    
}