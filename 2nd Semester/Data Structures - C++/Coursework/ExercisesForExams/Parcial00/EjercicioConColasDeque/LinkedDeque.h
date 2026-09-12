#pragma once

#include <iostream>
#include <stdexcept>
#include "Deque.h"
#include "Node.h"

template<typename E>
class LinkedDeque : public Deque<E>
{
private:
	Node<E>* front;
	Node<E>* back;
	int size;

public:

	LinkedDeque() {
		front = back = new Node<E>();
		size = 0;
	}

	~LinkedDeque() {
		clear();
		delete front;
	}

	void pushFront(E element) {
		front->next = new Node<E>(element, front->next);

		if (size == 0)
			back = front->next;

		size++;
	}

	void pushBack(E element) {
		back = back->next = new Node<E>(element);
		size++;
	}

	E popFront() {
		if (size == 0)
			throw std::runtime_error("Deque is empty.");

		E result = front->next->element;

		Node<E>* temp = front->next->next;

		delete front->next;
		front->next = temp;

		size--;

		if (size == 0)
			back = front;

		return result;
	}

	E popBack() {
		if (size == 0)
			throw std::runtime_error("Deque is empty.");

		E result = back->element;

		Node<E>* temp = front;

		while (temp->next != back) {
			temp = temp->next;
		}

		delete back;

		back = temp;
		back->next = nullptr;

		size--;

		return result;
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
		if (size == 0)
			throw std::runtime_error("Deque is empty. There's nothing to print.");

		std::cout << "[ ";

		for (Node<E>* temp = front->next; temp != nullptr; temp = temp->next) {
			std::cout << temp->element;

			if (temp->next != nullptr)
				std::cout << ", ";
		}

		std::cout << " ]" << '\n';
	}
};

