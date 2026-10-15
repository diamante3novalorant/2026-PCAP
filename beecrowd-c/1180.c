/*
Problema 1180 beecrowd
Faça um programa que leia um valor N. Este N será o tamanho de um vetor X[N]. 
depois faça com que ele identifique o menor número e a posição desse número dentro do vetor.
2026.10.14
Rodrigo
*/

#include <stdio.h>

int main(void) {
    int n;
    if (scanf("%d", &n) != 1) return 0;
    
    int v[n];
    int menor, pos = 0;
    
    for (int i = 0; i < n; i++) {
        scanf("%d", &v[i]);
        if (i == 0 || v[i] < menor) {
            menor = v[i];
            pos = i;
        }
    }
    
    printf("Menor valor: %d\n", menor);
    printf("Posicao: %d\n", pos);
    
    return 0;
}