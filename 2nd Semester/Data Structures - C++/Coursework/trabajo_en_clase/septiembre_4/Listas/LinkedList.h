#pragma once

#include <iostream>
#include <stdexcept>
#include "List.h"
#include "Node.h"

template<typename E>
class LinkedList : public List<E> {
private:
	Node<E>* head;
	Node<E>* tail;
	Node<E>* current;
	int size;

public:
	LinkedList() {
		tail = current = head = new Node<E>();
		size = 0;
	}

	~LinkedList() {
		clear();
		delete front;
	}

	void insert(E element) {
		current->next = new Node<E>(element, current->next);
		if (current == tail)
			tail = current->next;
		size++;
	}

	void append(E element) {
		tail = tail->next = new Node<E>(element);
		size++;
	}

	void setElement(E element) {
		if (size == 0)
			throw std::runtime_error("List is empty.");
		if (current == tail)
			throw std::runtime_error("No current element.");
		current->next->element = element;
	}

	E remove() {
		if (size == 0)
			throw std::runtime_error("List is empty.");
		E result = front->next->element;

		Node<E>* temp = current->next->next;
		delete current->next;
		current->next = temp;

		size--;
		if (size == 0)
			tail = current;

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
		tail = current = head;
	}

	E getElement() {
		if (size == 0)
			throw std::runtime_error("List is empty.");
		if (current == tail)
			throw std::runtime_error("No current element.");
		return current->next->element;
	}

	void goToStart() {
		current = head;
	}

	void goToEnd() {
		current = tail;
	}

	void goToPos(int pos) {
		if (pos >= size || pos < 0)
			throw std::runtime_error("Posicion invalida.");
		for (int i = 0; i <= pos; i++) {

		}
	}

	void next() {
		
	}

	void previous() {
		
	}

	bool atEnd() {
		
	}

	bool atStart() {
		
	}

	int getPos() {
		
	}

	int getSize() {
		
	}

	void print() {
		
	}

};

