/*
* Disciplina: 2026-PCAP
* Problema  : 2165 Beecrowd
* Autor     : Rodrigo
* LIAC      : Lê uma mensagem e verifica seu tamanho. Se possuir até 140 caracteres,
*             inclusive, pode ser publicada no Twitter; caso ultrapasse esse limite,
*             a mensagem não pode ser publicada.
*/

#include <iostream>
#include <string>
using namespace std;

int main() {
    string mensagem;

    getline(cin, mensagem);

    if (mensagem.size() <= 140)
        cout << "TWEET" << endl;
    else
        cout << "MUTE" << endl;

    return 0;
}