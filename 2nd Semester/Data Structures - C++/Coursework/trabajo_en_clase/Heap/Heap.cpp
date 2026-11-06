#include <iostream>
#include <string>
#include <cstdlib>
#include "MinHeap.h"
#include "HeapPriorityQueue.h"

int main() {
	std::cout << "Se le solicitara le tamano para la creacion de 2 heaps" << '\n';
	std::cout << "Escriba un numero entero positivo" << '\n';
	std::cout << "Tamano del primer heap:" << '\n';
	std::string respuesta1;
	int respuesta1Int;
	while (!(std::getline(
		std::cin >> std::ws, respuesta1)) || 
		std::stoi(respuesta1) < 1) {
		std::cin.clear();
		std::cout << "ERROR: Numero no valido, ";
		std::cout << "escriba un numero entero positivo" << '\n';
	}
	respuesta1Int = std::stoi(respuesta1);

	std::cout << "Tamano del segundo heap:" << '\n';
	std::string respuesta2;
	int respuesta2Int;
	while (!(std::getline(
		std::cin >> std::ws, respuesta2)) ||
		std::stoi(respuesta2) < 1) {
		std::cin.clear();
		std::cout << "ERROR: Numero no valido, ";
		std::cout << "escriba un numero entero positivo" << '\n';
	}
	respuesta2Int = std::stoi(respuesta2);

	srand(time(0));
	MinHeap<int>* heap1 = new MinHeap<int>();
	MinHeap<int>* heap2 = new MinHeap<int>();
	for (int i = 0; i < respuesta1Int; i++) {
		heap1->insert(rand() % 100);
	}

	for (int i = 0; i < respuesta2Int; i++) {
		heap2->insert(rand() % 100);
	}

	std::cout << "heap 1:" << '\n';
	heap1->print();
	std::cout << '\n';
	std::cout << "heap 2:" << '\n';
	heap2->print();
	std::cout << '\n';
	heap1->merge(heap2);
	std::cout << "heap 1 mergeado con el heap2:" << '\n';
	heap1->print();
	std::cout << '\n';

	std::cout << "Escriba un numero entero positivo" << '\n';
	std::cout << "Esa sera la cantidad de elementos a sacar el heap 1:" << '\n';
	std::string respuesta3;
	int respuesta3Int;
	while (!(std::getline(
		std::cin >> std::ws, respuesta3)) ||
		std::stoi(respuesta3) < 1) {
		std::cin.clear();
		std::cout << "ERROR: Numero no valido, ";
		std::cout << "escriba un numero entero positivo" << '\n';
	}
	respuesta3Int = std::stoi(respuesta3);

	std::cout << "Primeros " << respuesta3Int << " elementos del heap 1" << '\n';
	List<int>* lista = heap1->removeTop(respuesta3Int);
	lista->print();
	delete[] lista;
	while (!(heap1->isEmpty())) {
		std::cout << heap1->removeFirst() << '\n';
	}

	std::cout << "Escriba un numero entero positivo" << '\n';
	std::cout << "Esa sera la cantidad de elementos de un arreglo para heapifisiarlo:" << '\n';
	std::string respuesta4;
	int respuesta4Int;
	while (!(std::getline(
		std::cin >> std::ws, respuesta4)) ||
		std::stoi(respuesta4) < 1) {
		std::cin.clear();
		std::cout << "ERROR: Numero no valido, ";
		std::cout << "escriba un numero entero positivo" << '\n';
	}
	respuesta4Int = std::stoi(respuesta4);

	int* arr = new int[respuesta4Int];
	for (int i = 0; i < respuesta4Int; i++) {
		arr[i] = rand() % 100;
	}

	heap1->heapify(arr, respuesta4Int);
	std::cout << "Arreglo de " << respuesta4Int << " elementos aleatorios heapifisiada" << '\n';
	heap1->print();
	std::cout << "removeTop() de todos los elementos del heap que antes era un arreglo y lo heapifisie:" << '\n';
	List<int>* lista2 = heap1->removeTop(respuesta4Int);
	lista2->print();
	delete[] lista2;
	delete heap1;
	delete heap2;

	return 0;
}
