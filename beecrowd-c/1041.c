/*
Problema 1041 Beecrowd
faça um programa que lê do teclado um numero x e outro y e os mostra nas cordenadas do plano cartesiano
2026.10.06
Rodrigo
*/


#include <stdio.h>

int main(){
    float x,y;
    scanf("%f %f", &x, &y);

    if (x == 0 && y == 0) {
        printf("Origem\n");
    } else if (x > 0 && y < 0) {
        printf("Q4\n");
    } else if (x > 0 && y > 0) {
        printf("Q1\n");
    } else if (x < 0 && y < 0) {
        printf("Q3\n");
    } else if (x < 0 && y > 0) {
        printf("Q2\n");
    } else if (x == 0) {
        printf("Eixo Y\n");
    } else if (y == 0) {
        printf("Eixo X\n");
    }
    return 0;
}