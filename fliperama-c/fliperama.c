/*
* Disciplina: 2026-PCAP
* Projeto   : fliperama em C
* Autor     : Rodrigo Magagnin
* LIAC      : Validação e yap
*/

#include <stdio.h>

#define DONO "Rodrigo.Magagnin"

void linha() {
    printf("================================================================\n") ;
}

void titulo(char texto[]){
    linha();
    printf("    %s\n", texto);
    linha();
}

int ler_numero(char mensagem[], int minimo, int maximo) {
    int numero, lidos;

    printf("      %s:", mensagem);
    lidos = scanf ("%d", &numero);
    while (lidos != 1 || numero< minimo || numero > maximo){
        if (lidos !=1){
            scanf("%*s");
        }
        printf("Opção Inválida! Tente de novo:");
        lidos = scanf("%d", &numero);
    }
    return numero;
}

void mostrar_menu() {
    linha();
    printf(" FLIPERAMA DO %s\n", DONO);
    linha();
    printf("[1] Adivinhe o Número\n");
    printf("[2] Cadastrar Jogador\n");
    printf("[3] Listar Jogadores\n");
    printf("[0] Sair\n");
    linha();
}






int main(){
    int opcao;

    mostrar_menu();
    opcao = ler_numero("Tu escolha", 0, 3);
    while (opcao !=0){
        if (opcao == 1) {
            printf("O jogo entra na fase #.\n");
        } else if (opcao == 2 ){
            printf (" O cadastro entra na fase 2.\n");            
        } else {
            printf("A lista entra na fase 2.\n");
        }
        mostrar_menu();
        opcao = ler_numero("Tua escolha", 0, 3);
    }
    titulo("Até a próxima!");
    return 0;
}