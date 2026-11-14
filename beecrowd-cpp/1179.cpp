/*
* Disciplina: 2026-PCAP
* Problema  : 1179 Beecrowd
* Autor     : Rodrigo
* LIAC      : Lê 15 números inteiros e separa pares e ímpares em vetores distintos.
*             Sempre que um vetor atingir cinco elementos, imprime seus valores
*             e reinicia sua contagem. Ao final, imprime os elementos restantes,
*             primeiro os ímpares e depois os pares.
*/

#include <iostream>
using namespace std;

int main() {
    int par[5], impar[5];
    int p = 0, im = 0;

    for (int i = 0; i < 15; i++) {
        int x;
        cin >> x;

        if (x % 2 == 0) {
            par[p] = x;
            p++;

            if (p == 5) {
                for (int j = 0; j < 5; j++)
                    cout << "par[" << j << "] = " << par[j] << endl;

                p = 0;
            }
        } else {
            impar[im] = x;
            im++;

            if (im == 5) {
                for (int j = 0; j < 5; j++)
                    cout << "impar[" << j << "] = " << impar[j] << endl;

                im = 0;
            }
        }
    }

    for (int i = 0; i < im; i++)
        cout << "impar[" << i << "] = " << impar[i] << endl;

    for (int i = 0; i < p; i++)
        cout << "par[" << i << "] = " << par[i] << endl;

    return 0;
}