/*
* Disciplina: 2026-PCAP
* Problema  : 2059 Beecrowd
* Autor     : Rodrigo
* LIAC      : Lê os valores que indicam a escolha dos jogadores, se o jogador 1
*             roubou e se o jogador 2 acusou. Verifica primeiro as condições de
*             roubo e acusação; se nenhuma delas ocorrer, determina o vencedor
*             pela paridade da soma dos números escolhidos.
*/

#include <iostream>
using namespace std;

int main() {
    int p, j1, j2, r, a;

    cin >> p >> j1 >> j2 >> r >> a;

    if (r == 1 && a == 1) {
        cout << "Jogador 2" << endl;
    } else if (r == 1 || a == 1) {
        cout << "Jogador 1" << endl;
    } else {
        int soma = j1 + j2;

        if (soma % 2 == 0) {
            if (p == 1)
                cout << "Jogador 1" << endl;
            else
                cout << "Jogador 2" << endl;
        } else {
            if (p == 0)
                cout << "Jogador 1" << endl;
            else
                cout << "Jogador 2" << endl;
        }
    }

    return 0;
}