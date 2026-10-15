/*
Problema 1114 Beecrowd
crie um progama que lê uma senha de 4 números e recusa o acesso até que esteja correta
2026.10.14
Rodrigo
*/

#include <stdio.h>

int main() {
  int s;
  scanf("%d", &s);
  while (s != 2002) {
    printf("Senha Invalida\n");
    scanf("%d", &s);
  }
  printf("Acesso Permitido\n");
  return 0;
}