/*
Problema 1043 Beecrowd: Crie um programa que calcule se os numeros podem formar um triangulo, se podem,
calcule o perimetro dele, e se não podem, calcule a área do trapézio.
2026.09.02
Rodrigo
*/

#include <stdio.h>

int main() {
    double A, B, C;
    scanf("%lf %lf %lf", &A, &B, &C);

    if (A < B + C && B < A + C && C < A + B) {
        printf("Perimetro = %.1lf\n", A + B + C);
    } else {
        double area = ((A + B) * C) / 2.0;
        printf("Area = %.1lf\n", area);
    }

    return 0;
}