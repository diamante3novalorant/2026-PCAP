/*
Problema 1067 Beecrowd
Crie um programa que lê um número x e mostra todos os números impares até ele, incluindo-o se for impar também
2026.10.14
Rodrigo
*/
#include <stdio.h>

int main() {
    int X;
    scanf("%d", &X);
    
    for (int i = 1; i <= X; i++) {
        if (i % 2 != 0) {
            printf("%d\n", i);
        }
    }
    return 0;
}
