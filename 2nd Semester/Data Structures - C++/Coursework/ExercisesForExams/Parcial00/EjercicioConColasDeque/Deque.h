#pragma once

template<typename E>
class Deque
{
public:
	Deque(const Deque<E>&) = delete;
	void operator=(const Deque<E>&) = delete;
	Deque() {}
	virtual ~Deque() {}
	virtual void pushFront(E) = 0;
	virtual void pushBack(E) = 0;
	virtual E popFront() = 0;
	virtual E popBack() = 0;
	virtual void clear() = 0;
	virtual bool isEmpty() = 0;
	virtual int getSize() = 0;
	virtual void print() = 0;
};

