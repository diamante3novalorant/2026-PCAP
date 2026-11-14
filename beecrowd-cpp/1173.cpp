/*
* Disciplina: 2026-PCAP
* Problema  : 1173 Beecrowd
* Autor     : Rodrigo
* LIAC      : Lê um valor inteiro para a primeira posição do vetor. As posições
*             seguintes recebem o valor da posição anterior dividido por dois,
*             utilizando divisão inteira, até completar 10 elementos.
*/

#include <iostream>
using namespace std;

int main() {
    int n[10];

    cin >> n[0];

    for (int i = 1; i < 10; i++) {
        n[i] = n[i - 1] / 2;
    }

    for (int i = 0; i < 10; i++) {
        cout << "N[" << i << "] = " << n[i] << endl;
    }

    return 0;
}