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
    int N;
    int X[10];

    cin >> N;

    X[0] = N;

    for (int i = 1; i < 10; i++) {
        X[i] = X[i - 1] * 2;
    }

    for (int i = 0; i < 10; i++) {
        cout << "N[" << i << "] = " << X[i] << endl;
    }

    return 0;
}
