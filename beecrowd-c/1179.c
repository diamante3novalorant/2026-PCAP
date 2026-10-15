/*
Problema 1179 beecrowd
crie um programa que: leia um número e veja se ele é par ou ímpar,guarde o número na lista certa,
quando a lista encher mostre todos os números que estão nela na tela, esvazie essa lista para que ela possa receber novos números
e quando acabarem todos os 15 numeros mostre o que sobrou na lista de ímpares e de pares.
2026.10.14
Rodrigo
*/

#include <stdio.h>

int main() {
    int par[5], impar[5];
    int j = 0, k = 0, num;

    for (int i = 0; i < 15; i++) {
        scanf("%d", &num);

        if (num % 2 == 0) {
            par[j] = num;
            j++;
            if (j == 5) {
                for (int x = 0; x < 5; x++) {
                    printf("par[%d] = %d\n", x, par[x]);
                }
                j = 0;
            }
        } else {
            impar[k] = num;
            k++;
            if (k == 5) {
                for (int x = 0; x < 5; x++) {
                    printf("impar[%d] = %d\n", x, impar[x]);
                }
                k = 0;
            }
        }
    }

    // Imprimir o que sobrou no vetor ímpar primeiro, depois no par
    for (int x = 0; x < k; x++) {
        printf("impar[%d] = %d\n", x, impar[x]);
    }
    for (int x = 0; x < j; x++) {
        printf("par[%d] = %d\n", x, par[x]);
    }

    return 0;
}