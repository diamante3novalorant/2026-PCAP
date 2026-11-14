/*
* Disciplina: 2026-PCAP
* Problema  : 1178 Beecrowd
* Autor     : Rodrigo
* LIAC      : Lê um valor real e preenche um vetor com 100 posições. Cada posição
*             seguinte recebe metade do valor da posição anterior. Os resultados
*             são apresentados com quatro casas decimais.
*/

#include <iostream>
using namespace std;

int main() {
    double n[100];

    cin >> n[0];

    for (int i = 1; i < 100; i++) {
        n[i] = n[i - 1] / 2.0;
    }

    cout.precision(4);
    cout << fixed;

    for (int i = 0; i < 100; i++) {
        cout << "N[" << i << "] = " << n[i] << endl;
    }

    return 0;
}