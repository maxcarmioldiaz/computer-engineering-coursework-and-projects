#include <iostream>
#include <cstdlib>
#include "Matrix.h"

int main()
{
    srand(time(0));

    Matrix<int> *matriz1 = new Matrix<int>(10, 15);
    for (int i = 0; i < matriz1->getRows(); i++) {
        for (int j = 0; j < matriz1->getColumns(); j++) {
            matriz1->setValue(i, j, rand() % 100);
        }
    }

    Matrix<int>* matriz2 = new Matrix<int>(10, 15);
    for (int i = 0; i < matriz2->getRows(); i++) {
        for (int j = 0; j < matriz2->getColumns(); j++) {
            matriz2->setValue(i, j, rand() % 100);
        }
    }
    
    std::cout << "Matriz 1: " << '\n';
    matriz1->print();
    std::cout << '\n';

    std::cout << "Matriz 2: " << '\n';
    matriz2->print();
    std::cout << '\n';

    Matrix<int>* sumaMatrices = new Matrix<int>(10, 15);
    for (int i = 0; i < sumaMatrices->getRows(); i++) {
        int* filaMatriz1 = matriz1->getRowElements(i);
        int* filaMatriz2 = matriz2->getRowElements(i);
        for (int j = 0; j < sumaMatrices->getColumns(); j++) {
            sumaMatrices->setValue(i, j, filaMatriz1[j] + filaMatriz2[j]);
        }
    }

    std::cout << "Suma matrices: " << '\n';
    sumaMatrices->print();
    std::cout << '\n';


    delete matriz1;
    delete matriz2;
    delete sumaMatrices;
    return 0;
}

