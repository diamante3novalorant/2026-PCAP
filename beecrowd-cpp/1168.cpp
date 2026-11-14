/*
* Disciplina: 2026-PCAP
* Problema  : 1168 Beecrowd
* Autor     : Rodrigo
* LIAC      : Lê a quantidade de casos e, para cada número, calcula quantos LEDs
*             são necessários para representá-lo. Percorre cada dígito e soma
*             sua quantidade correspondente de LEDs, utilizando um vetor de apoio.
*/

#include <iostream>
#include <string>
using namespace std;

int main() {
    int n;
    int leds[] = {6, 2, 5, 5, 4, 5, 6, 3, 7, 6};

    cin >> n;

    while (n--) {
        string numero;
        int total = 0;

        cin >> numero;

        for (char c : numero) {
            total += leds[c - '0'];
        }

        cout << total << " leds" << endl;
    }

    return 0;
}