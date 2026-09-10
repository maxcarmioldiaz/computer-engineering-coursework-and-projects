#pragma once

#include <iostream>
#include <stdexcept>
#include "PriorityQueue.h"
#include "LinkedQueue.h"

template <typename E>
class LinkedPriorityQueue : public PriorityQueue<E>
{
private:
	LinkedQueue<E>* queues;
	int priorities;
	int size;

public:
	LinkedPriorityQueue(int priorities = 20) {
		if (priorities < 0)
			throw std::runtime_error("Priorities should be a positive integer.");
		this->priorities = priorities;
		this->queues = new LinkedQueue<E>[priorities];
		size = 0;
	}

	~LinkedPriorityQueue() {
		delete[] queues;
	}

	void insert(E element, int priority) {
		if (priority >= priorities || priority < 0)
			throw std::runtime_error("Invalid priority.");

		queues[priority].enqueue(element);

		size++;
	}

	E min() {
		for (int i = 0; i < priorities; i++) {
			if (queues[i].getSize() != 0)
				return queues[i].frontValue();
		}
		throw std::runtime_error("There's no elements in any of the queues.");
	}

	E removeMin() {
		for (int i = 0; i < priorities; i++) {
			if (queues[i].getSize() != 0) {
				size--;
				return queues[i].dequeue();
			}
		}
		throw std::runtime_error("There's no elements in any of the queues.");
	}

	void clear() {
		for (int i = 0; i < priorities; i++) {
			queues[i].clear();
		}
		size = 0;
	}

	int getSize() {
		return size;
	}

	bool isEmpty() {
		return size == 0;
	}

	void print() {
		for (int i = 0; i < priorities; i++) {
			std::cout << i + 1 << ": ";
			queues[i].print();
			std::cout << '\n';
		}
	}
};

