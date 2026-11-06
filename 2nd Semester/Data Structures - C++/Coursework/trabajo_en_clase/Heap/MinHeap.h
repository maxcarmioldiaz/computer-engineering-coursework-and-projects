#pragma once

#include <stdexcept>
#include <iostream>
#include "Includes.h"

template<typename E>
class MinHeap {
private:
	E* elements;
	int max;
	int size;

	int parent(int pos) {
		return (pos - 1) / 2;
	}

	int leftChild(int pos) {
		return pos * 2 + 1;
	}

	int rightChild(int pos) {
		return leftChild(pos) + 1;
	}

	bool isLeaf(int pos) {
		return leftChild(pos) >= size;
	}

	void swap(int pos1, int pos2) {
		E temp = elements[pos1];
		elements[pos1] = elements[pos2];
		elements[pos2] = temp;
	}

	void siftUp(int pos) {
		while (pos > 0 && elements[pos] < elements[parent(pos)]) {
			swap(pos, parent(pos));
			pos = parent(pos);
		}
	}

	int minChild(int pos) {
		int right = rightChild(pos);
		int left = leftChild(pos);
		if (right < size && elements[right] < elements[left])
			return right;
		return left;
	}

	void siftDown(int pos) {
		while (!isLeaf(pos) && elements[minChild(pos)] < elements[pos]) {
			int min = minChild(pos);
			swap(min, pos);
			pos = min;
		}
	}

	void restrictionIsEmpty() {
		if (size == 0)
			throw std::runtime_error("Heap is empty");
	}

	void restrictionIsFull() {
		if (size == max)
			throw std::runtime_error("Heap is full.");
	}

	void restrictionPosDoesntExist(int pos) {
		if (pos < 0 || pos >= size)
			throw std::runtime_error("Index out of bounds");
	}

public:
	MinHeap<E>(int max = DEFAULT_MAX) {
		if (max < 1)
			throw std::runtime_error("Invalid max size");
		this->elements = new E[max];
		this->max = max;
		size = 0;
	}

	~MinHeap() {
		delete[] elements;
	}

	void insert(E element) {
		restrictionIsFull();
		elements[size] = element;
		siftUp(size);
		size++;
	}

	E first() {
		restrictionIsEmpty();
		return elements[0];
	}

	E removeFirst() {
		restrictionIsEmpty();
		return remove(0);
	}

	E remove(int pos) {
		restrictionIsEmpty();
		restrictionPosDoesntExist(pos);
		swap(pos, size - 1);
		size--;
		siftDown(pos);
		return elements[size];
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
		std::cout << "[ ";
		for (int i = 0; i < size; i++) {
			std::cout << elements[i];
			if (i < size - 1)
				std::cout << ", ";
		}
		std::cout << " ]" << '\n';
	}

	void heapify(E* ar, int n) {}

	void merge(MinHeap<E>* other) {}

	List<E>* removeTop(int n) {}

};

