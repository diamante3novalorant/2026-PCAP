/*
* Disciplina: 2026-PCAP
* Problema  : 1176 Beecrowd
* Autor     : Rodrigo
* LIAC      : Lê a quantidade de casos e, para cada um, calcula o termo da sequência
*             de Fibonacci solicitado. Utiliza um vetor previamente preenchido,
*             começando por 0 e 1, somando os dois termos anteriores para gerar
*             os próximos valores.
*/

#include <iostream>
using namespace std;

int main() {
    unsigned long long fib[61];

    fib[0] = 0;
    fib[1] = 1;

    for (int i = 2; i <= 60; i++) {
        fib[i] = fib[i - 1] + fib[i - 2];
    }

    int t;
    cin >> t;

    while (t--) {
        int n;
        cin >> n;

        cout << "Fib(" << n << ") = " << fib[n] << endl;
    }

    return 0;
    
}