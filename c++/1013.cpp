<<<<<<< HEAD
#include <stdio.h>
#include <math.h>

int main() {
 
    int A, B, C;
    char line[50];
    int maior_parcial, maior_total;

    fgets(line, sizeof(line), stdin);
    sscanf(line, "%d %d %d", &A, &B, &C);

    maior_parcial = (A + B + abs(A - B)) / 2;

    maior_total = (maior_parcial + C + abs(maior_parcial - C)) / 2;

    printf("%d eh o maior\n", maior_total);
 
    return 0;
=======
#include <stdio.h>
#include <math.h>

int main() {
 
    int A, B, C;
    char line[50];
    int maior_parcial, maior_total;

    fgets(line, sizeof(line), stdin);
    sscanf(line, "%d %d %d", &A, &B, &C);

    maior_parcial = (A + B + abs(A - B)) / 2;

    maior_total = (maior_parcial + C + abs(maior_parcial - C)) / 2;

    printf("%d eh o maior\n", maior_total);
 
    return 0;
>>>>>>> 1cfb7856b5cd16d06c82bd088e56144c1fd011c8
}