/*
Problema 1078 beecrowd: crie um programa que lê um inteiro de entrada e mostre o quadrado de cada valor par até chegar nele
por exemplo: 6, o programa deve calcular 2, 4 e 6 ao quadrado.
2026.10.14
Rodrigo
*/

#include <stdio.h>

int main() {
    int n, i;
    scanf("%d", &n);
    for (i = 2; i <= n; i += 2) {
        printf("%d^2 = %d\n", i, i * i);
    }
    return 0;
}