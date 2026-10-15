/*
Problema 1175 beecrowd
Faça um programa que leia um vetor N[20] e troque o primeiro numero com o ultimo etc...
2026.10.14
Rodrigo
*/

#include <stdio.h>

int main() {
    int n[20], i, aux;

    // Leitura dos 20 valores
    for (i = 0; i < 20; i++) {
        scanf("%d", &n[i]);
    }

    // Inversão dos elementos (troca até a metade: 10 elementos)
    for (i = 0; i < 10; i++) {
        aux = n[i];
        n[i] = n[19 - i];
        n[19 - i] = aux;
    }

    // Impressão do vetor modificado
    for (i = 0; i < 20; i++) {
        printf("N[%d] = %d\n", i, n[i]);
    }

    return 0;
}

