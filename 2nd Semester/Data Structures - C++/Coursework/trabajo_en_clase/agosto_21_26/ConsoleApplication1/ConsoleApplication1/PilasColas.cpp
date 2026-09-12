#include <iostream>
#include "ArrayStack.h"
#include "LinkedStack.h"
#include "ArrayQueue.h"
#include "LinkedQueue.h"

int main() {
	Queue<int>* cola = new LinkedQueue<int>();
	cola->enqueue(45);
	cola->enqueue(56);
	cola->enqueue(67);
	cola->enqueue(78);
	cola->enqueue(89);
	cola->print();
	cola->enqueue(100);
	cola->print();
	std::cout << "dequeue: " << cola->dequeue() << std::endl;
	std::cout << "dequeue: " << cola->dequeue() << std::endl;
	std::cout << "dequeue: " << cola->dequeue() << std::endl;
	cola->print();
	std::cout << "frontValue: " << cola->frontValue() << std::endl;
	cola->enqueue(89);
	cola->enqueue(12);
	cola->enqueue(23);
	cola->enqueue(34);
	cola->enqueue(45);
	cola->clear();
	cola->print();

	delete cola;

	return 0;
}