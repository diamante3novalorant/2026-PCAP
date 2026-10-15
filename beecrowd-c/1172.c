/*
Problema 1172 beecrowd
Faça um programa que leia um vetor X[10] e substitua todos os valores negativos e zero por 1
depois mostre.
2026.10.14
Rodrigo
*/

#include <stdio.h>

int main() {
    int X[10];
    for (int i = 0; i < 10; i++) {
        scanf("%d", &X[i]);
        if (X[i] <= 0) {
            X[i] = 1;
        }
    }
    for (int i = 0; i < 10; i++) {
        printf("X[%d] = %d\n", i, X[i]);
    }
    return 0;
}