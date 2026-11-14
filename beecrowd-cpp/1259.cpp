/*
* Disciplina: 2026-PCAP
* Problema  : 1259 Beecrowd
* Autor     : Rodrigo
* LIAC      : Lê uma quantidade de números inteiros e separa os valores em dois
*             vetores: pares e ímpares. Ordena os pares em ordem crescente e os
*             ímpares em ordem decrescente, imprimindo primeiro os pares.
*/

#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

int main() {
    int n;
    cin >> n;

    vector<int> pares, impares;

    for (int i = 0; i < n; i++) {
        int x;
        cin >> x;

        if (x % 2 == 0)
            pares.push_back(x);
        else
            impares.push_back(x);
    }

    sort(pares.begin(), pares.end());
    sort(impares.begin(), impares.end(), greater<int>());
    for (int x : pares)
        cout << x << endl;

    for (int x : impares)
        cout << x << endl;

    return 0;
}