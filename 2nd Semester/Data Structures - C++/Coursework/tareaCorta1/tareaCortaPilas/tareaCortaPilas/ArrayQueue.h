#pragma once

#include <stdexcept>
#include <iostream>
#include "Queue.h"
#include "Includes.h"

template<typename E>

class ArrayQueue : public Queue<E> {
private:
	E* elements;
	int front;
	int back;
	int max;
	int size;

public:
	ArrayQueue(int max = DEFAULT_MAX) {
		if (max < 1)
			throw std::runtime_error("Invalid max size.");
		elements = new E[max];
		this->max = max;
		front = back = size = 0;
	}

	~ArrayQueue() {
		delete[] elements;
	}

	void enqueue(E element) {
		if (size == max)
			throw std::runtime_error("Queue is full.");
		elements[back] = element;
		back = (back + 1) % max;
		size++;
	}

	E dequeue() {
		if (size == 0)
			throw std::runtime_error("Queue is empty.");
		front = (front + 1) % max;
		size--;
		return elements[(front + max - 1) % max];
	}

	E frontValue() {
		if (size == 0)
			throw std::runtime_error("There's no front value.");
		return elements[front];
	}

	void clear() {
		size = 0;
	}

	bool isEmpty() {
		return size == 0;
	}

	int getSize() {
		if (size == 0)
			return 0;
		return size;
	}

	void print() {
		if (size == 0)
			throw std::runtime_error("Can't print, queue is empty.");

		std::cout << "[ ";
		int index = front;
		while (index != back - 1) {
			std::cout << elements[index] << ", ";
			index = (index + 1) % max;
		}
		std::cout << elements[back - 1] << " ]" << std::endl;
	}
};