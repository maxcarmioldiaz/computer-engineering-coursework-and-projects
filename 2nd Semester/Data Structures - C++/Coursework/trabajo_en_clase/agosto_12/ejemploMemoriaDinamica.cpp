#include <iostream>
#include <cstdlib>

using std::cout;
using std::cin;
using std::endl;

int main() 
{
    int tamano;

    cout << "Indique el tamaño del arreglo: ";

    cin >> tamano;

    int* numeros = new int[tamano];

    srand(time(0));

    int suma = 0;
    for (int i = 0; i < tamano; i++) 
    {
        numeros[i] = rand() % 100;
        suma += numeros[i];
    }

    for (int i = 0; i < tamano; i++) 
    {
        cout << "pos " << i << ":" << numeros[i] << endl;
    }

    double promedio = (double)suma / (double) tamano
    
    cout << "Promedio: " << promedio

    delete[] numeros;

    return 0;
}