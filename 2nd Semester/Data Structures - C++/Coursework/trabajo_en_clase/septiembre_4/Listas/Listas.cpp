#include <iostream>
#include <cstdlib>
#include "ArrayList.h"


int main()
{
	List<int>* listaNumeros = new ArrayList<int>(20);
	for (int i = 0; i < 20; i++) {
		std::cout << std::endl << "tamano: " << listaNumeros->getSize() << "  posicion: " << listaNumeros->getPos() << std::endl;
		listaNumeros->append(i);
		listaNumeros->print();
	}
	listaNumeros->clear();
	listaNumeros->print();

	for (int i = 20; i > 0; i--) {
		std::cout << std::endl << "tamano: " << listaNumeros->getSize() << "  posicion: " << listaNumeros->getPos() << std::endl;
		listaNumeros->append(i);
		listaNumeros->print();
	}

	listaNumeros->goToEnd();

	while (!listaNumeros->atStart()) {
		listaNumeros->previous();
		std::cout << listaNumeros->getElement() << std::endl;
	}

	delete listaNumeros;
}