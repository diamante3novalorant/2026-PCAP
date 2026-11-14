/*
* Disciplina: 2026-PCAP
* Problema  : 1332 Beecrowd
* Autor     : Rodrigo
* LIAC      : Lê palavras que representam números escritos em inglês. Compara
*             a quantidade de letras e os caracteres de cada palavra para
*             identificar se o número é 1, 2 ou 3.
*/

#include <iostream>
#include <string>
using namespace std;

int main() {
    int n;
    cin >> n;

    while (n--) {
        string palavra;
        cin >> palavra;

        if (palavra.size() == 5) {
            cout << 3 << endl;
        } else if (palavra[0] == 'o' && palavra[1] == 'n' ||
                   palavra[0] == 'o' && palavra[2] == 'e' ||
                   palavra[1] == 'n' && palavra[2] == 'e') {
            cout << 1 << endl;
        } else {
            cout << 2 << endl;
        }
    }

    return 0;
}