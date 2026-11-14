/*
* Disciplina: 2026-PCAP
* Problema  : 1180 Beecrowd
* Autor     : Rodrigo
* LIAC      : Lê a quantidade de elementos de um vetor e seus respectivos valores.
*             Percorre o vetor procurando o menor número e guarda sua posição,
*             considerando que o primeiro elemento está na posição zero.
*/

#include <iostream>
using namespace std;

int main() {
    int n;
    cin >> n;

    int x[1000];

    for (int i = 0; i < n; i++) {
        cin >> x[i];
    }

    int menor = x[0];
    int posicao = 0;

    for (int i = 1; i < n; i++) {
        if (x[i] < menor) {
            menor = x[i];
            posicao = i;
        }
    }

    cout << "Menor valor: " << menor << endl;
    cout << "Posicao: " << posicao << endl;

    return 0;
}