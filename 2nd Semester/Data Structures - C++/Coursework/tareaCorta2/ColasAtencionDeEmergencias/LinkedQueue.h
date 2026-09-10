#pragma once

#include <stdexcept>
#include <iostream>
#include "Queue.h"
#include "Node.h"

template <typename E>

class LinkedQueue : public Queue<E>
{
private:
	Node<E>* front;
	Node<E>* back;
	int size;

public:

	LinkedQueue() {
		front = back = new Node<E>();
		size = 0;
	}

	~LinkedQueue() {
		clear();
		delete front;
	}

	void enqueue(E element) {
		back = back->next = new Node<E>(element);
		size++;
	}

	E dequeue() {
		if (size == 0)
			throw std::runtime_error("Queue is empty.");
		E result = front->next->element;
		Node<E>* temp = front->next->next;
		delete front->next;
		front->next = temp;
		size--;
		if (size == 0)
			back = front;
		return result;
	}

	E frontValue() {
		if (size == 0)
			throw std::runtime_error("Queue is empty.");
		return front->next->element;
	}

	void clear() {
		Node<E>* temp;
		while (front->next != nullptr) {
			temp = front->next->next;
			delete front->next;
			front->next = temp;
		}
		size = 0;
		back = front;
	}

	bool isEmpty() {
		return size == 0;
	}

	int getSize() {
		return size;
	}
	void print() {
		std::cout << "[ ";
		for (Node<E>* temp = front->next; temp != nullptr; temp = temp->next) {
			std::cout << temp->element;
			if (temp->next != nullptr)
				std::cout << ", ";
		}

		//while (front->next != nullptr) {
			//temp = front->next->next;
		//}

		std::cout << " ]";
	}
};

