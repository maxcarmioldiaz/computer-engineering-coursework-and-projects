package logic;

import java.time.LocalDate;
import java.util.List;
import java.util.LinkedList;

public class Libro {
private String titulo;
private LocalDate fechaPublicacion;
private String isbn;
private String editorial;
private List<Autor> autores;

public Libro(String titulo, LocalDate fechaPublicacion, String isbn, String editorial) {
	super();
	this.titulo = titulo;
	this.fechaPublicacion = fechaPublicacion;
	this.isbn = isbn;
	this.editorial = editorial;
	this.autores = new LinkedList<>();
}

public String getTitulo() {
	return titulo;
}

public void setTitulo(String titulo) {
	this.titulo = titulo;
}

public LocalDate getFechaPublicacion() {
	return fechaPublicacion;
}

public void setFechaPublicacion(LocalDate fechaPublicacion) {
	this.fechaPublicacion = fechaPublicacion;
}

public String getIsbn() {
	return isbn;
}

public void setIsbn(String isbn) {
	this.isbn = isbn;
}

public String getEditorial() {
	return editorial;
}

public void setEditorial(String editorial) {
	this.editorial = editorial;
}

public void addAutor(Autor autor ) {
	this.autores.add(autor);
}

public void addAutor(String name, String country, LocalDate fechaNac, LocalDate fechaFac) {
	Autor autor = new Autor(name, country, fechaNac, fechaFac);
	this.autores.add(autor);
}

public void addAutor(String name, String country, LocalDate fechaNac) {
	Autor autor = new Autor(name, country, fechaNac);
	this.autores.add(autor);
}

public void deleteAutor(int pos) throws Exception {
	if (pos < 0 || pos >= autores.size())
		throw new Exception("Posicion de autor no valida.");
	autores.remove(pos);
}

public String toString() {
	String myString = "Libro(" + titulo + ", " + isbn + ", " + editorial + ", Autores: ";
	
	int i = 1;
	for (Autor autor : autores) {
		myString += autor.toString();
		if (i != autores.size()) {
			myString += ", ";
		}
		
		i += 1;
	}
	
	return myString;
}

}
