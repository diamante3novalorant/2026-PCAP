/*
* Disciplina: 2026-PCAP
* Problema  : 1049 Beecrowd - Animal
* Autor     : Rodrigo
* LIAC      : Lê três características de um animal e utiliza
*             estruturas condicionais if e else para identificar
*             qual animal corresponde às informações recebidas.
*             Primeiro verifica se é vertebrado ou invertebrado,
*             depois analisa seu grupo e sua alimentação para
*             determinar e imprimir o animal correspondente.
*/

#include <iostream>
#include <string>
using namespace std;

int main() {
    string p1, p2, p3;

    cin >> p1 >> p2 >> p3;

    if (p1 == "vertebrado") {
        if (p2 == "ave") {
            if (p3 == "carnivoro")
                cout << "aguia" << endl;
            else
                cout << "pomba" << endl;
        } else {
            if (p3 == "onivoro")
                cout << "homem" << endl;
            else
                cout << "vaca" << endl;
        }
    } else {
        if (p2 == "inseto") {
            if (p3 == "hematofago")
                cout << "pulga" << endl;
            else
                cout << "lagarta" << endl;
        } else {
            if (p3 == "hematofago")
                cout << "sanguessuga" << endl;
            else
                cout << "minhoca" << endl;
        }
    }

    return 0;
}