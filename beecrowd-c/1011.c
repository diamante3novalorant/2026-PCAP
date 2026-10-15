/*
Problema 1011 Beecrowd
faça um programa que calcule o volume de uma esfera utilizando double.
2026.09.02
Rodrigo
*/
#include <stdio.h>
 
int main() {
    double r,v,pi ;
    scanf("%lf", &r);
    v = (4.0/3.0) * 3.14159 * (r*r*r) ;
    printf("VOLUME = %.3lf\n", v) ;
 
    return 0;
}