/*
Problema 1164 beecrowd
O programa deve ler um inteiro e ver se ele é a soma de todos os numeros que vem antes dele, o que caracteriza um nº perfeito.
2026.10.14
Rodrigo
*/
#include <stdio.h>

int main() {
    int N, X, soma;
    
    scanf("%d", &N);
    
    for (int i = 0; i < N; i++) {
        scanf("%d", &X);
        soma = 0;
        
        // Testa os divisores de 1 até X - 1
        for (int j = 1; j < X; j++) {
            if (X % j == 0) {
                soma += j;
            }
        }
        
        if (soma == X) {
            printf("%d eh perfeito\n", X);
        } else {
            printf("%d nao eh perfeito\n", X);
        }
    }
    
    return 0;
}