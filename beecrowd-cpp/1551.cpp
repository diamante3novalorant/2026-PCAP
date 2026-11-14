/*
* Disciplina: 2026-PCAP
* Problema  : 1551 Beecrowd
* Autor     : Rodrigo
* LIAC      : Lê frases e verifica quantas letras diferentes do alfabeto aparecem.
*             Utiliza um vetor de controle para evitar contar letras repetidas.
*             Com 26 letras, a frase é completa; com pelo menos 13, quase completa;
*             abaixo disso, é considerada mal elaborada.
*/

#include <iostream>
#include <string>
#include <cctype>
using namespace std;

int main() {
    int n;
    cin >> n;
    cin.ignore();

    while (n--) {
        string frase;
        bool letras[26] = {false};
        int total = 0;

        getline(cin, frase);

        for (char c : frase) {
            if (isalpha(static_cast<unsigned char>(c))) {
                int pos = tolower(static_cast<unsigned char>(c)) - 'a';

                if (!letras[pos]) {
                    letras[pos] = true;
                    total++;
                }
            }
        }

        if (total == 26)
            cout << "frase completa" << endl;
        else if (total >= 13)
            cout << "frase quase completa" << endl;
        else
            cout << "frase mal elaborada" << endl;
    }

    return 0;
}