/*
Problema 1006 Beecrowd
faça um programa que calcule a média de 3 inteiros sendo que c vale mais que b e b vale mais que a
2026.09.02
Rodrigo
*/

#include <stdio.h>
 
int main() {
    double A, B, C, MEDIA;
    scanf("%lf",&A) ;
    scanf("%lf", &B) ;
    scanf("%lf", &C) ;
    MEDIA = (A * 2 + B * 3 + C * 5) / 10;
    printf("MEDIA = %.1lf\n", MEDIA) ;
    return 0;
}