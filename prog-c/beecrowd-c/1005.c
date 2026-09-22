/*
Problema 1005 Beecrowd
2026.09.02
Rodrigo
*/
#include <stdio.h>

int main() {
    float A, B, MEDIA;
    scanf("%f",&A) ;
    scanf("%f", &B) ;
    MEDIA = (A * 3.5 + B * 7.5) / 11;
    printf("MEDIA = %.5f\n", MEDIA) ;
    return 0;
}