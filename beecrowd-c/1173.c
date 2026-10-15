/*
Problema 1173 beecrowd
Leia um valor e faça um programa que põe o valor lido na primeira posição de um vetor N[10] e vai dobrando nas proximas
por exemplo:
input = 200 | N[0] = 200
            | N[1] = 400
e continua.
2026.10.14
Rodrigo
*/
#include <stdio.h>

int main() {
    int n[10], i, x, k;
    
    scanf("%d", &x);
    
    for (k = 0, i = x; k < 10; i *= 2, k++) {
        n[k] = i;
    }
    
    for (i = 0; i < 10; i++) {
        printf("N[%d] = %d\n", i, n[i]);
    }
    
    return 0;
}