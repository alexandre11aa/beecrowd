#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int main() {

    int money_notas, money_moedas;
    double input_money;
    char str_money[50];

    scanf("%lf", &input_money);

    sprintf(str_money, "%.10g", input_money);

    sscanf(str_money, "%d.%d", &money_notas, &money_moedas);

    int n100 = money_notas / 100;

    int n50  = (money_notas - n100 * 100) / 50;

    int n20  = (money_notas - n100 * 100 - n50 * 50) / 20;

    int n10  = (money_notas - n100 * 100 - n50 * 50 - n20 * 20) / 10;

    int n5   = (money_notas - n100 * 100 - n50 * 50 - n20 * 20 - n10 * 10) / 5;

    int n2   = (money_notas - n100 * 100 - n50 * 50 - n20 * 20 - n10 * 10 - n5 * 5) / 2;

    int m100 = (money_notas - n100 * 100 - n50 * 50 - n20 * 20 - n10 * 10 - n5 * 5 - n2 * 2);

    int m50  = money_moedas / 50;

    int m25  = (money_moedas - m50 * 50) / 25;

    int m10  = (money_moedas - m50 * 50 - m25 * 25) / 10;

    int m5   = (money_moedas - m50 * 50 - m25 * 25 - m10 * 10) / 5;

    int m1   = (money_moedas - m50 * 50 - m25 * 25 - m10 * 10 - m5 * 5);

    printf("NOTAS:\n");
    printf("%d nota(s) de R$ 100.00\n", n100);
    printf("%d nota(s) de R$ 50.00\n", n50);
    printf("%d nota(s) de R$ 20.00\n", n20);
    printf("%d nota(s) de R$ 10.00\n", n10);
    printf("%d nota(s) de R$ 5.00\n", n5);
    printf("%d nota(s) de R$ 2.00\n", n2);
    printf("MOEDAS:\n");
    printf("%d moeda(s) de R$ 1.00\n", m100);
    printf("%d moeda(s) de R$ 0.50\n", m50);
    printf("%d moeda(s) de R$ 0.25\n", m25);
    printf("%d moeda(s) de R$ 0.10\n", m10);
    printf("%d moeda(s) de R$ 0.05\n", m5);
    printf("%d moeda(s) de R$ 0.01\n", m1);

}