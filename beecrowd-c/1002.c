/*
Problema 1002 Beecrowd
faça um programa que calcule a área do circulo
2026.09.29
Rodrigo
*/

#include <stdio.h>
int main() {
    double area, n, raio ;
    n = 3.14159 ;
    scanf("%lf" , &raio) ;
    area = (n * (raio*raio)) ;
    printf ("A=%.4lf\n",area) ;
}