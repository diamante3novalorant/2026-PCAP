#include <stdio.h>
int main(){
    printf("Hello World!\n") ;
    
    int num1, num2, soma ;
    printf("Digite um número: ") ;
    scanf("%d", &num1) ;
    printf("Digite outro número: ") ;
    scanf("%d", &num2) ;
    soma = num1 + num2 ;
    printf("A soma desses 2 números é: %d\n", soma) ;

    return 0;

}
