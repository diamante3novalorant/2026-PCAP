/*
Problema 1165 Beecrowd
o programa deve ler um número e ver se ele é primo ou não
2026.10.14
Rodrigo
*/

#include <stdio.h>

int main() {
    int n, x, i, j, eh_primo;

    scanf("%d", &n);

    for (i = 0; i < n; i++) {
        scanf("%d", &x);
        eh_primo = 1; // assume que é primo

        if (x <= 1) {
            eh_primo = 0;
        } else {
            // Testa divisores de 2 até x - 1
            for (j = 2; j < x; j++) {
                if (x % j == 0) {
                    eh_primo = 0;
                    break;
                }
            }
        }

        if (eh_primo) {
            printf("%d eh primo\n", x);
        } else {
            printf("%d nao eh primo\n", x);
        }
    }

    return 0;
}