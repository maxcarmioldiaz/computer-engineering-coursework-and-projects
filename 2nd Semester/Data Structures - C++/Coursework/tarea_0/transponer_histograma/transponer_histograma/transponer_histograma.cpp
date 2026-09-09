// transponer_histograma.cpp : This file contains the 'main' function. Program execution begins and ends there.
//

#include <iostream>
#include <string>

void myPrinter(int array, int array_size);

int main()
{
    int n;

    std::cout << "Programa para transponer un histograma no decreciente." << s'\n';

    std::cout << "Indique la cantidad de numeros a leer: ";

    while (!(std::cin >> n) || n < 1) {
        std::cout << "Debe ingresar un numero entero positivo (es decir, mayor o igual a 1)";
    }

    int* integer_list = new int[n];

    std::cout << "Ingrese los enteros, deben estar en orden no decreciente." << '\n';
    for (int i = 0; i < n; i++) {
        std::cout << "Entero " << i+1 << ": ";
        int n_temp;
        std::cin >> n_temp;
        integer_list[i] = n_temp;
    }

    int columns = integer_list[n - 1];

    std::string* matrix = new std::string[n][columns];

    for (int filas = 0; filas < n; filas++) {
        int quantity = integer_list[filas];
        for (int cols = 0; cols < columns - 1; cols++) {
            for (int q = 0; q < quantity + 1; q++) {
                matrix[filas][cols] = "*";
                cols++;
            }
            matrix[filas][cols] = "0";
        }
    }

    myPrinter(integer_list, n);
    delete[] integer_list;

    std::string* trans_matrix = new std::string[columns][n];

    int* trans_list = new int[columns];

    for (int filas = n - 1; filas > -1; filas--) {
        int cols_trans = 0;

        for (int cols = columns - 1; cols > -1; cols--) {
            int filas_trans = 0;

            if (matrix[filas][cols] == "*") {
                trans_matrix[filas_trans][cols_trans] = "*";
            }
            trans_matrix[filas_trans][cols_trans] = "0";
            filas_trans++;
        }
        cols_trans++;
    }
    delete[] matrix;
    
    for (int filas = 0; filas < n; filas++) {
        int quantity = 0;

        for (int cols = 0; cols < columns; cols++) {

            if (trans_matrix[filas][cols] == "*") {
                quantity++;
            }
        }

        trans_list[filas] = quantity;
    }
    delete[] trans_matrix;


    myPrinter(trans_list, columns);
    delete[] trans_list;

    return 0;
}

void myPrinter(int array, int array_size)
{
    std::cout << "[";
    for (int i = 0; i < array_size - 1; i++) {
        std::cout << " " << array[i] << ",";
    }
    std::cout << " " << array[array_size - 1] << " ]" << '\n';

    for (int i = 0; i < array_size; i++) {
        for (int k = 0; k < array[i]; k++) {
            std::cout << "*";
        }
        std::cout << '\n';
    }
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
