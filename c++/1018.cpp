#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int main() {

    int a, n100, n50 = 0, n20 = 0, n10 = 0, n5 = 0, n2 = 0, n1 = 0;
    double n_temp;
    char n_temp_str[50];

    scanf("%d", &a);

    printf("%d\n", a);

    while (true) {
        if (a == 0) {
            break;
        }

        if (a >= 100) {
            n_temp = a / 100.0;

            sprintf(n_temp_str, "%.10g", n_temp);

            sscanf(n_temp_str, "%d.%d", &n100, &a);

        } else if (a >= 50) {
            n50 += 1;
            a -= 50; 

        } else if (a >= 20) {
            n20 += 1;
            a -= 20; 

        } else if (a >= 10) {
            n10 += 1;
            a -= 10; 

        } else if (a >= 5) {
            n5 += 1;
            a -= 5;  

        } else if (a >= 2) {
            n2 += 1;
            a -= 2;

        } else {
            n1 += 1;
            a -= 1;  
        }
    }

    printf("%d nota(s) de R$ 100,00\n", n100);
    printf("%d nota(s) de R$ 50,00\n", n50);
    printf("%d nota(s) de R$ 20,00\n", n20);
    printf("%d nota(s) de R$ 10,00\n", n10);
    printf("%d nota(s) de R$ 5,00\n", n5);
    printf("%d nota(s) de R$ 2,00\n", n2);
    printf("%d nota(s) de R$ 1,00\n", n1);

}