#include <iostream>
#include <string>
#include "MinHeap.h"
#include "HeapPriorityQueue.h"

int main() {
	PriorityQueue<std::string>* cursos = new HeapPriorityQueue<std::string>();
	cursos->insert("Comunicacion", 1000);
	cursos->insert("Mate Discreta", 3);
	cursos->insert("Arquitectura", 1);
	cursos->insert("Calculo", 3);
	cursos->insert("Estructuras de Datos", 0);
	cursos->insert("Ajedrez", 7);
	cursos->insert("P.O.O.", 6);
	cursos->insert("F.O.C.", 0);
	cursos->insert("Accion Social", 1000);
	cursos->print();
	std::string respuesta;
	while (!cursos->isEmpty()) {
		std::cout << "Estudiando: " << cursos->removeMin() << '\n';
		cursos->print();
		getline(std::cin, respuesta);
	}
	std::cout << "Fin de los cursos." << '\n';
	delete cursos;
	return 0;
}
