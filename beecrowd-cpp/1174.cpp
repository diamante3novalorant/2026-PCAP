/*
* Disciplina: 2026-PCAP
* Problema  : 1174 Beecrowd
* Autor     : Rodrigo
* LIAC      : Lê 100 valores reais e armazena cada um em um vetor. Depois percorre
*             os elementos e imprime somente aqueles que forem menores ou iguais
*             a 10, indicando também a posição e apresentando uma casa decimal.
*/

#include <iostream>
using namespace std;

int main() {
    double a[100];

    for (int i = 0; i < 100; i++) {
        cin >> a[i];
    }

    for (int i = 0; i < 100; i++) {
        if (a[i] <= 10) {
            cout << "A[" << i << "] = ";
            cout << fixed;
            cout.precision(1);
            cout << a[i] << endl;
        }
    }

    return 0;
}