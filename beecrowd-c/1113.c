/*
Problema 1113 beecrowd
crie um programa que lê um par de números digitados e mostra se eles estão em ordem crescente ou decrescente
2026.10.14
Rodrigo
*/

#include <stdio.h>

int main() {
    int x, y;
    while (scanf("%d %d", &x, &y) != EOF && x != y) {
        if (x < y) {
            printf("Crescente\n");
        } else {
            printf("Decrescente\n");
        }
    }
    return 0;
}

