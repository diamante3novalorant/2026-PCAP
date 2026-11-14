/*
* Disciplina: 2026-PCAP
* Problema  : 1001 Beecrowd
* Autor     : Rodrigo 
* LIAC      : Faça um programa que calcule e mostre o volume de uma esfera sendo fornecido o valor de seu raio (R)
*/
#include <iostream>
#include <iomanip>
using namespace std;

int main() {
    double R, volume;
    

    cin >> R;

    volume = (4.0 / 3.0) * 3.14159 * R * R * R;

    cout << fixed << setprecision(3);
    cout << "VOLUME = " << volume << endl;

    return 0;
}