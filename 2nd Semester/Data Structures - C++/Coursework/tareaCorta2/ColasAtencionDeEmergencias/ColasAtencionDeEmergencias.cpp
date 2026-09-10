#include <iostream>
#include "LinkedPriorityQueue.h"
#include "Patient.h"

void deleteObjects(PriorityQueue<Patient>* attentionQueue);
PriorityQueue<Patient>* addPatient(PriorityQueue<Patient>* attentionQueue);
PriorityQueue<Patient>* attendPatient(PriorityQueue<Patient>* attentionQueue);
bool isValidId(std::string id);
bool isValidPriority(int level);
bool isValidChar(char c);

int main()
{
	PriorityQueue<Patient>* attentionQueue = new LinkedPriorityQueue<Patient>(5);

	bool running = 1;
	while (running) {
		std::cout << "TRIAGE - Cola de espera:" << '\n';
		attentionQueue->print();
		std::cout << '\n';

		std::cout << "1. Ingresar paciente" << '\n';
		std::cout << "2. Atender paciente" << '\n';
		std::cout << "3. Salir" << '\n';
		std::cout << "Opcion: ";
		std::string option;

		while (!std::getline(std::cin >> std::ws, option) || (option != "1" && option != "2" && option != "3")) {
			//Chequeo de restricciones
			std::cin.clear();
			std::cout << '\n';

			//Se hace la solicitud de la opcion de nuevo
			std::cout << "Elija alguna de las 3 opciones escribiendo un 1, 2 o 3" << '\n';
			std::cout << "1. Ingresar paciente" << '\n';
			std::cout << "2. Atender paciente" << '\n';
			std::cout << "3. Salir" << '\n';
			std::cout << "Opcion: ";
		}
		std::cin.clear();
		std::cout << '\n';

		if (option == "1")
		{
			attentionQueue = addPatient(attentionQueue);
		}

		else if (option == "2")
		{
			attentionQueue = attendPatient(attentionQueue);
		}

		else 
		{ 
			std::cout << '\n' << '\n' << "Gracias por usar el programa :D" << '\n' << '\n';
			running = 0;
		}
	}

	deleteObjects(attentionQueue);
}

void deleteObjects(PriorityQueue<Patient>* array) {
	array->clear();
	delete[] array;
}


bool isValidChar(char c) {
	return c == '1' || c == '2' || c == '3' || c == '4' || c == '5' || c == '6' || c == '7' || c == '8' || c == '9' || c == '0' || c == '-';
}

bool isValidId(std::string id) {
	for (char c : id) {
		if (!isValidChar(c))
			return 0;
		}
		return 1;
	}

bool isValidPriority(int level) {
	return level == 1 || level == 2 || level == 3 || level == 4 || level == 5;
}

PriorityQueue<Patient>* addPatient(PriorityQueue<Patient>* attentionQueue) {
	std::cout << "Ingresar datos del paciente" << '\n';
	std::cout << "ID: ";
	std::string id;
	while (!std::getline(std::cin >> std::ws, id) || !isValidId(id)) {
		//Chequeo de restricciones
		std::cin.clear();
		std::cout << '\n';

		//Se hace la solicitud del ID de nuevo
		std::cout << "El ID ingresado no es valido." << '\n';
		std::cout << "Ingrese un ID valido, solo se permiten numeros y guiones" << '\n';
		std::cout << '\n';
		std::cout << "ID: ";
	}
	
	std::cout << "CONDICION (1-Azul, 2-Rojo, 3-Amarillo, 4-Verde, 5-Blanco): ";
	int level;
	while (!(std::cin >> level) || !isValidPriority(level)) {
		//Chequeo de restricciones
		std::cin.clear();
		std::cin.ignore(std::numeric_limits<std::streamsize>::max(), '\n');
		std::cout << '\n';

		//Se hace la solicitud del level de nuevo
		std::cout << "El nivel de prioridad ingresada no es valida." << '\n';
		std::cout << "Ingrese un nivel de prioridad valido, solo se permiten numeros del 1 al 5." << '\n';
		std::cout << '\n';
		std::cout << "CONDICION (1-Azul, 2-Rojo, 3-Amarillo, 4-Verde, 5-Blanco): ";
	}

	Patient p(id, level);

	try { 
		attentionQueue->insert(p, level - 1); 
	} catch (std::runtime_error& e) {

	}
	
	return attentionQueue;
}

PriorityQueue<Patient>* attendPatient(PriorityQueue<Patient>* attentionQueue) {
	Patient p = attentionQueue->removeMin();
	p.attend();
	p.print();

	return attentionQueue;
}