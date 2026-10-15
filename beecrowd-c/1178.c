/*
Problema 1178 beecrowd
Leia um valor X e põe o valor na primeira posição de um vetor N[100] e na proxima 
posição vai dividindo pela metade, por exemplo
200.0000 = N[0] = 200.0000
           N1[1] = 100.0000 e vai indo.
2026.10.14
Rodrigo
*/

#include <stdio.h>

int main() {
    double b;
    scanf("%lf", &b);
    for (int i = 0; i < 100; i++) {
        printf("N[%d] = %.4lf\n", i, b);
        b = b / 2.0;
    }
    return 0;
}