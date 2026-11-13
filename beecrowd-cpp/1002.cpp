/*
* Disciplina: 2026-PCAP
* Problema  : 1002 Beecrowd
* Autor     : Rodrigo 
* LIAC      : Lê o raio R (real). Calcula a área com pi = 3.14159 e imprime "A=area" com 4 casas.
*/

#include <iostream>
#include <iomanip>
using namespace std;

int main(){
    double r,area;
    
    cin >> r;
    area = 3.14159 * r * r;
    cout << fixed << setprecision(4);
    cout << "A=" << area << endl;

    return 0;

}