/*
* Disciplina: 2026-PCAP
* Problema  : 1234 Beecrowd
* Autor     : Rodrigo
* LIAC      : Lê frases até o fim da entrada e alterna letras maiúsculas e
*             minúsculas, começando com maiúscula. Espaços e outros caracteres
*             são mantidos sem alterar a alternância entre as letras.
*/

#include <iostream>
#include <string>
#include <cctype>
using namespace std;

int main() {
    string frase;

    while (getline(cin, frase)) {
        bool maiuscula = true;

        for (char &c : frase) {
            if (isalpha(static_cast<unsigned char>(c))) {
                if (maiuscula)
                    c = toupper(static_cast<unsigned char>(c));
                else
                    c = tolower(static_cast<unsigned char>(c));

                maiuscula = !maiuscula;
            }
        }

        cout << frase << endl;
    }

    return 0;
}