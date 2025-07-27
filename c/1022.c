#include <stdio.h>

int MDC(int numero_1, int numero_2) {
    int denominador_comum;
    
    if (numero_1 <= numero_2) {
        denominador_comum = numero_1;
    } else {
        denominador_comum = numero_2;
    }
    
    while (1) {
        if ((numero_1 % denominador_comum == 0) && (numero_2 % denominador_comum == 0)) {
            return denominador_comum;
        }
        
        denominador_comum--;
    }
}

int main() {
    
    int N;
    
    scanf("%d", &N);
    
    int i;
    
    for (i = 0; i < N; i++) {
        
        int N1, N2, D1, D2;
        
        char sinal;
        
        scanf("%d %*c %d %c %d %*c %d", &N1, &D1, &sinal, &N2, &D2);
        
        int NC, NS, DC, DS;
    
        if (sinal == '+') {
            NC = N1 * D2 + N2 * D1;
            DC = D1 * D2;
        } else if (sinal == '-') {
            NC = N1 * D2 - N2 * D1;
            DC = D1 * D2;
        } else if (sinal == '*') {
            NC = N1 * N2;
            DC = D1 * D2;
        } else {
            NC = N1 * D2;
            DC = N2 * D1;
        }
        
        int denominador_comum = MDC(NC, DC);
        
        if (denominador_comum < 0) {
            denominador_comum = denominador_comum * -1;
        }
        
        NS = NC / denominador_comum;
        DS = DC / denominador_comum;
        
        printf("%d/%d = %d/%d\n", NC, DC, NS, DS);
        
    }
    
    return 0;
}
