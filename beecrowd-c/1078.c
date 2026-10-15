/*
Problema 1078 beecrowd: crie um programa que lê um inteiro de entrada e mostre a tabuada desse numero.
2026.10.14
Rodrigo
*/


#include <stdio.h>

    int main() {
        int n,i;

        scanf("%d", &n);

        for(i = 1; i <= 10; i ++) {
        printf("%d x %d = %d\n", i, n, i * n);
    }    

    return 0;
}