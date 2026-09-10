#pragma once

#include <stdexcept>
#include <iostream>
#include <string>
#include <time.h>

class Patient
{
private:
	std::string id;
	int level;
	time_t arrival;
	time_t attended;
	time_t waitingTime;

public:
	Patient(std::string id, int level) {
		this->id = id;
		this->level = level;
		this->arrival = time(nullptr);
	}

	Patient() {}

	void attend() {
		this->attended = time(nullptr);
		this->waitingTime = (time_t)difftime(attended, arrival);
	}

	void print() {
		std::cout << "ID: " << id << '\n';
		std::cout << "CONDICION: " << level << " ";

		if (level == 1)
			std::cout << "AZUL - Resucitacion";
		else if (level == 2)
			std::cout << "ROJO - Emergencia";
		else if (level == 3)
			std::cout << "AMARILLO - Urgente";
		else if (level == 4) {
			std::cout << "VERDE - Menos urgente"; 

		} else {
			std::cout << "BLANCO - No urgente";
		}

		std::cout << '\n';

		std::tm arrivalTm;
		std::tm attendedTm;

		localtime_s(&arrivalTm, &arrival);
		localtime_s(&attendedTm, &attended);

		std::cout << "LLEGADA: " << arrivalTm.tm_hour << ":" << arrivalTm.tm_min << ":" << arrivalTm.tm_sec << '\n';
		std::cout << "ATENDIDO: " << attendedTm.tm_hour << ":" << attendedTm.tm_min << ":" << attendedTm.tm_sec << '\n';

		std::cout << "ESPERA: ";


		if (waitingTime >= 3600) {
			int hours = waitingTime / 3600;
			std::cout << hours << "h ";
		}
		if (waitingTime >= 60) {
			int minutes = (waitingTime % 3600 ) / 60;
			std::cout << minutes << "m ";
		}
		waitingTime = waitingTime % 60;
		std::cout << waitingTime << "s " << '\n';
	}

	friend std::ostream& operator<<(std::ostream& os, Patient p) {
		os << "(Id: " << p.id << ", Nivel: " << p.level << ")";
		return os;
	}

};

