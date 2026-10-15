/*
Problema 1153 beecrowd
Leia um valor N e calcule seu fatorial
2026.10.14
Rodrigo
*/

#include <stdio.h>

int main() {
    int N, i, fatorial = 1;
    scanf("%d", &N);
    for (i = N; i >= 1; i--) {
        fatorial = fatorial * i;
    }
    printf("%d\n", fatorial);
    return 0;
}