#pragma once

#include <iostream>
#include <stdexcept>
#include "Deque.h"
#include "Includes.h"

template<typename E>
class ArrayDeque : public Deque<E>
{
private:
	E* elements;
	int front;
	int back;
	int max;
	int size;

public:
	ArrayDeque(int max = DEFAULT_MAX) {
		if (max < 1)
			throw std::runtime_error("Invalid max size.");
		elements = new E[max];
		this->max = max;
		front = back = size = 0;
	}

	~ArrayDeque() {
		delete[] elements;
	}

	void pushFront(E element) {
		if (size == max)
			throw std::runtime_error("Deque is full.");
		
		if (front - 1 >= 0) {
			front = front - 1;
		}
		else {
			front = max - 1;
		}
		elements[front] = element;
		size++;
	}

	void pushBack(E element) {
		if (size == max)
			throw std::runtime_error("Deque is full.");
		elements[back] = element;
		back = (back + 1) % max;
		size++;
	}

	E popFront() {
		if (size == 0)
			throw std::runtime_error("Queue is empty.");
		front = (front + 1) % max;
		size--;
		return elements[(front + max - 1) % max];
	}

	E popBack() {
		if (size == 0)
			throw std::runtime_error("Queue is empty.");
		if (back == 0) {
			back = max - 1;
		} else { 
			back = back - 1; 
		}
		
		size--;
		return elements[back];
	}

	void clear() {
		size = 0;
	}

	bool isEmpty() {
		return size == 0;
	}

	int getSize() {
		return size;
	}

	void print() {
		if (size == 0)
			throw std::runtime_error("Can't print, queue is empty.");

		std::cout << "[ ";

		for (int i = 0; i < size; i++) {
			std::cout << elements[(front + i) % max];
			if (i < size - 1)
				std::cout << ", ";
		}
		std::cout << " ]" << '\n';
	}
};

