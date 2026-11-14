/*
* Disciplina: 2026-PCAP
* Problema  : 1548 Beecrowd
* Autor     : Rodrigo
* LIAC      : Lê a quantidade de alunos e suas notas, mantendo a ordem original.
*             Cria uma cópia das notas e ordena em ordem decrescente. Compara as
*             duas sequências para contar quantos alunos permanecem na mesma posição.
*/

#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

int main() {
    int n;
    cin >> n;

    while (n--) {
        int m;
        cin >> m;

        vector<int> notas(m);
        vector<int> ordenadas(m);

        for (int i = 0; i < m; i++) {
            cin >> notas[i];
            ordenadas[i] = notas[i];
        }

        sort(ordenadas.begin(), ordenadas.end(), greater<int>());

        int total = 0;

        for (int i = 0; i < m; i++) {
            if (notas[i] == ordenadas[i]) {
                total++;
            }
        }

        cout << total << endl;
    }

    
    return 0;
}