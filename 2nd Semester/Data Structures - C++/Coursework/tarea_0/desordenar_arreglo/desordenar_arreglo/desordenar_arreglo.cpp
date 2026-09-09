// desordenar_arreglo.cpp : This file contains the 'main' function. Program execution begins and ends there.
//

#include <iostream>
#include <cstdlib>

using std::cout;
using std::cin;
using std::endl;

int main()
{
    int n;

    cout << "Indique la cantidad de numeros a generar (debe ingresar un numero mayor que 2): ";

    while (!(cin >> n) || n <= 2 ) {
        cin.clear();
        cin.ignore(10000, '\n');
           
        cout << "Ingrese un numero, este debe ser mayor a 2." << endl;

        cout << "Indique la cantidad de numeros a generar (debe ingresar un numero mayor que 2): ";
    }

    int* array = new int[n];

    for (int i = 0; i < n; i++) {
        array[i] = i+1;
    }

    srand(time(0));

    int* array_desordenado = new int[n];

    for (int i = 0; i < n; i++) {
        array_desordenado[i] = i + 1;
    }

    for (int i = 0; i < n/2+1; i++) {
        int index1 = rand() % n;
        int index2 = rand() % n;
        while (index1 == index2) {
            index2 = rand() % n;
        }
        int cambio = array_desordenado[index1];
        array_desordenado[index1] = array_desordenado[index2];
        array_desordenado[index2] = cambio;
    }

    printf("%-30s", "Arreglo ordenado:");
    cout << "[";
    for (int i = 0; i < n-1; i++) {
        cout << " " << array[i] << ",";
    }
    cout << " " << array[n-1] << " ]" << endl;

    printf("%-30s", "Arreglo desordenado:");
    cout << "[";
    for (int i = 0; i < n-1; i++) {
        cout << " " << array_desordenado[i] << ",";
    }
    cout << " " << array_desordenado[n - 1] << " ]" << endl;

    delete[] array_desordenado;
    delete[] array;

    return 0;
}

// Run program: Ctrl + F5 or Debug > Start Without Debugging menu
// Debug program: F5 or Debug > Start Debugging menu

// Tips for Getting Started: 
//   1. Use the Solution Explorer window to add/manage files
//   2. Use the Team Explorer window to connect to source control
//   3. Use the Output window to see build output and other messages
//   4. Use the Error List window to view errors
//   5. Go to Project > Add New Item to create new code files, or Project > Add Existing Item to add existing code files to the project
//   6. In the future, to open this project again, go to File > Open > Project and select the .sln file
