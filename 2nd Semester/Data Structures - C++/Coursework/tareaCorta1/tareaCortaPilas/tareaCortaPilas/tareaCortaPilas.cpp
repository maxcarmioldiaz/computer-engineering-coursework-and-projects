#include <iostream>
#include <limits>
#include <string>
#include "ArrayStack.h"
#include "LinkedStack.h"

std::string reader();
std::string nextToken(std::string expression);
std::string type(std::string token);
int precedence(char op);
bool isOperatorOrParenthesis(char element);
double processOperation(Stack<double>* nStack, Stack<char>* charStack);
void pusherAndProcesser(Stack<double>* nStack, Stack<char>* charStack, std::string expression);
void myPrinter(Stack<double>* nStack, Stack<char>* charStack, std::string expression);

int main() {
	std::string option;
	//Se pregunta que opcion se va a utilizar, si Array o Linked Stack
	std::cout << "Que tipo de pila desea usar? (Responda con un 1 o un 2)" << '\n';
	std::cout << "1. ArrayStack" << '\n';
	std::cout << "2. LinkedStack" << '\n';
	std::cout << "Eleccion: ";
	while (!std::getline(std::cin >> std::ws, option) || (option != "1" && option != "2")) {
		//Chequeo de restricciones
		std::cin.clear();
		std::cout << '\n';

		//Se hace la solicitud de la opcion de nuevo
		std::cout << "Elija alguna de las 2 opciones escribiendo un 1 o un 2" << '\n';
		std::cout << "Que tipo de pila desea usar? (Responda con un 1 o un 2)" << '\n';
		std::cout << "1. ArrayStack" << '\n';
		std::cout << "2. LinkedStack" << '\n';
		std::cout << "Eleccion: ";
	}
	std::cin.clear();
	std::cout << '\n';

	//Se evalua si la eleccion fue Array Stack
	if (option == "1") {
		//Se crea el Array
		Stack<double>* nStack = new ArrayStack<double>(5);
		Stack<char>* charStack = new ArrayStack<char>(5);

		//Se lee la expresion
		std::string expression = reader();

		pusherAndProcesser(nStack, charStack, expression);
	}

	//Gracias a que se restringio cualquier otra opcion
	// que no fuera 1 o 2 si no se elegio el 1 estrictamente
	// se eligio el 2 es decir Linked Stack

	else {
		Stack<double>* nStack = new LinkedStack<double>();
		Stack<char>* charStack = new LinkedStack<char>();

		//Se lee la expresion
		std::string expression = reader();

		pusherAndProcesser(nStack, charStack, expression);
		
	}
	return 0;
}

bool isOperatorOrParenthesis(char element) {
	return element == '*' || element == '/' || element == '+' || element == '-' || element == '^' || element == '(' || element == ')';
}

std::string reader() {
	std::string expression;
	std::cout << "Ingrese la expresion a analizar: ";
	std::cin >> expression;
	while ( !(std::cin.peek() == '\n') ) {
		std::string tempString;
		std::cin >> tempString;
		expression = expression + tempString;
	}
	return expression;
}

std::string type(std::string token) {
	if (isOperatorOrParenthesis(token[0])) {
		std::string tokenType = "op";
		return tokenType;
	}
	else {
		std::string tokenType = "dbl";
		return tokenType;
	}
}

int precedence(char op) {
	if (op == '+' || op == '-') {
		int precedenceValue = 0;
		return precedenceValue;
	}
	if (op == '*' || op == '/') {
		int precedenceValue = 1;
		return precedenceValue;
	}
	if (op == '^') {
		int precedenceValue = 2;
		return precedenceValue;
	}
}

std::string nextToken(std::string expression) {
	std::string token{ expression[0] };

	if (isOperatorOrParenthesis(expression[0])) {
		return token;
	}
	else if (expression.length() == 1){
		return token;
	}
	else {
		int i = 1;
		while (!(isOperatorOrParenthesis(expression[i]))) {
			std::string tempString(1, expression[i]);
			token += tempString;
			i++;
		}
	}
	return token;
}

double processOperation(Stack<double>* nStack, Stack<char>* charStack) {
	double result;
	double B = nStack->pop();
	double A = nStack->pop();
	char op = charStack->pop();

	switch (op) {
		case '+':
			result = A + B;
			std::cout << "Procesando operacion " << A << op << B << "=" << result << '\n';
			return result;

		case '-':
			result = A - B;
			std::cout << "Procesando operacion " << A << op << B << "=" << result << '\n';
			return result;

		case '*':
			result = A * B;
			std::cout << "Procesando operacion " << A << op << B << "=" << result << '\n';
			return result;

		case '/':
			if (B != 0) {
				result = A / B;
				std::cout << "Procesando operacion " << A << op << B << "=" << result << '\n';
				return result;
			}
			else { 
				std::cout << A << op << B << '\n' << "No se puede dividir entre 0. Error en la operacion.";
				return 0; 
			}

		case '^':
			result = pow(A, B);
			std::cout << "Procesando operacion " << A << op << B << "=" << result << '\n';
			return result;

		default:
			return 0;
	}
}

void myPrinter(Stack<double>* nStack, Stack<char>* charStack, std::string expression) {
	std::cout << "Pila numeros:             ";
	nStack->print();
	std::cout << "Pila operadores:          ";
	charStack->print();
	std::cout << "Expresion:                " << expression << '\n';
	std::cout << '\n';
	return;
}

void pusherAndProcesser(Stack<double>* nStack, Stack<char>* charStack, std::string expression) {
	myPrinter(nStack, charStack, expression);

	while (expression != "") {
		std::string tokenType;
		std::string token;

		token = nextToken(expression);
		std::cout << "Token actual: " << token << '\n';

		expression.erase(0, token.length());

		tokenType = type(token);

		if (tokenType == "dbl") {
			std::cout << "Es numero." << '\n' << "Push en la pila de numeros" << '\n';
			nStack->push(std::stod(token));
		}
		else {
			if (charStack->getSize() != 0 && charStack->topValue() != '(' && precedence(charStack->topValue()) >= precedence(token[0])) {
				std::cout << "Es operador." << '\n';
				std::cout << "Operador " << charStack->topValue() << " tiene precedencia mayor o igual que " << token << "." << '\n';
				double operation = processOperation(nStack, charStack);
				nStack->push(operation);
				std::cout << '\n';
				std::cout << "Push en la pila de operadores" << '\n';
				charStack->push(token[0]);
			}
			else if (token == ")") {
				if (charStack->topValue() != '(') {
					std::cout << "Es parentesis derecho." << '\n' << "Tope de la pila no es (." << '\n';

					double operation = processOperation(nStack, charStack);
					nStack->push(operation);

					std::cout << '\n';

					std::cout << "Pop en la pila de operadores: " << charStack->pop() << '\n';
				}
			}
			else {
				if (token == "(") {
					std::cout << "Es parentesis izquierdo." << '\n' << "Push en la pila de operadores" << '\n';
				}
				else {
					std::cout << "Es operador." << '\n' << "Push en la pila de operadores" << '\n';
				}
				charStack->push(token[0]);
			}
		}
		myPrinter(nStack, charStack, expression);
	}

	std::cout << "Fin de la expresion, procesando lo que queda en las pilas." << '\n';

	bool flag = !(charStack->isEmpty());
	double operation;
	while (flag) {

		if (!(nStack->getSize() == 1 && charStack->getSize() > 0)) {
			operation = processOperation(nStack, charStack);
			nStack->push(operation);
			myPrinter(nStack, charStack, expression);
			flag = !(charStack->isEmpty());
		}
		else {
			std::cout << "Hay un error en la expresion." << '\n';
			flag = 0;
		}

	}

	if (flag != 0)
		std::cout << "El resultado de la evaluacion es: " << operation << '\n';

}