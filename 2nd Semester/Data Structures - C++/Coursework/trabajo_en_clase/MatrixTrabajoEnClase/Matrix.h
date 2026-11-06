#pragma once
#include <stdexcept>


template <typename E>
class Matrix {
private:
	int rows;
	int columns;
	E** matrix;

	void restriction(int row, int column) {
		if (row < 0 || row >= rows)
			throw std::runtime_error("Invalid row");
		if (column < 0 || column >= columns)
			throw std::runtime_error("Invalid column");
	}

public:
	Matrix(int rows, int columns) {
		if (rows <= 0 || columns <= 0)
			throw std::runtime_error("Number of rows and columns must be greater than zero.");
		this->rows = rows;
		this->columns = columns;
		matrix = new E* [rows];
		for (int i = 0; i < rows; i++) {
			matrix[i] = new E[columns];
		}
	}

	~Matrix() {
		for (int i = 0; i < rows; i++) {
			delete[] matrix[i];
		}
		delete[] matrix;
	}

	E getValue(int row, int column) {
		restriction(row, column);
		return matrix[row][column];
	}

	void setValue(int row, int column, E value) {
		restriction(row, column);

		matrix[row][column] = value;
	}

	int getRows() {
		return rows;
	}

	int getColumns() {
		return columns;
	}

	void setAll(E value) {
		for (int i = 0; i < rows; i++) {
			for (int j = 0; j < columns; j++) {
				matrix[i][j] = value;
			}
		}
	}

	void transpose() {
		E** transposedMatrix = new E * [columns];
		for (int i = 0; i < columns; i++) {
			transposedMatrix[i] = new E[rows];
		}

		for (int i = 0; i < columns; i++) {
			for (int j = 0; j < rows; j++) {
				transposedMatrix[i][j] = matrix[j][i];
			}
		}

		for (int i = 0; i < rows; i++) {
			delete[] matrix[i];
		}
		delete[] matrix;

		this->matrix = transposedMatrix;
		int transposedColumns = rows;
		this->rows = columns;
		this->columns = transposedColumns;
	}

	void addRow(E value) {
		E** matrixExtraRow = new E * [rows + 1];
		for (int i = 0; i < rows; i++) {
			matrixExtraRow[i] = matrix[i] ;
		}
		matrixExtraRow[rows] = new E[columns];
		for (int j = 0; j < columns; j++) {
			matrixExtraRow[rows][j] = value;
		}
		delete[] matrix;

		this->matrix = matrixExtraRow;
		this->rows = rows + 1;
	}

	void addColumn(E value) {
		E** matrixExtraColumn = new E* [rows];
		for (int i = 0; i < rows; i++) {
			matrixExtraColumn[i] = new E [columns + 1];
		}
		for (int i = 0; i < rows; i++) {
			for (int j = 0; j < columns + 1; j++) {
				matrixExtraColumn[i][j] = matrix[i][j];
				if (j == columns) {
					matrixExtraColumn[i][j] = value;
				}
			}
		}

		delete[] matrix;

		this->matrix = matrixExtraColumn;
		this->columns = columns + 1;
	}

	E* getRowElements(int row) {
		E* rowElements = new E [columns];
		for (int j = 0; j < columns; j++) {
			rowElements[j] = matrix[row][j];
		}
		return rowElements;
	}

	E* getColumnElements(int column) {
		E* columnElements = new E [rows];
		for (int i = 0; i < rows; i++) {
			columnElements[i] = matrix[i][column];
		}
		return columnElements;
	}

	void print() {
		for (int i = 0; i < rows; i++) {
			for (int j = 0; j < columns; j++) {
				std::cout << matrix[i][j] << "\t";
			}
			std::cout << '\n';
		}
	}
};

