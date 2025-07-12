#include <stdio.h>
 
int main() {
    
    // Problema de Máximo Divisor Comúm (MDC)
 
    int N, i, F1, F2, r;
    
    scanf("%d", &N);
    
    for (i = 0; i < N; i++) {
        
        scanf("%d %d", &F1, &F2);
        
        while (F2 != 0) { 
            r = F1 % F2;
            F1 = F2;
            F2 = r;
        } // Algoritmo de Euclides
        
        printf("%d\n", F1);
    }
    
    return 0;
}
