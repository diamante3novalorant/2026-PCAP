/*
* Disciplina: 2026-PCAP
* Problema  : 2137 Beecrowd
* Autor     : Rodrigo
* LIAC      : Lê os códigos dos livros de cada conjunto de entrada e os armazena
*             em um vetor de strings. Utiliza a função sort para ordenar os códigos
*             em ordem crescente e imprime cada código, mantendo os zeros à esquerda.
*/

#include <iostream>
#include <vector>
#include <string>
#include <algorithm>
using namespace std;

int main() {
    int n;

    while (cin >> n) {
        vector<string> livros(n);

        for (int i = 0; i < n; i++) {
            cin >> livros[i];
        }

        sort(livros.begin(), livros.end());

        for (int i = 0; i < n; i++) {
            cout << livros[i] << endl;
        }
    }

    return 0;
}