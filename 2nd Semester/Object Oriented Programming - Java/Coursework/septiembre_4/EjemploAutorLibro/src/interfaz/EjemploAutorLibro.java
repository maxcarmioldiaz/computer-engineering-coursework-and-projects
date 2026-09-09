package interfaz;

import logic.Autor;
import logic.Libro;

import java.time.LocalDate;

public class EjemploAutorLibro {
	
	public static void main (String[] args) {
		Autor autor1 = new Autor("Stephen King", "Estados Unidos", LocalDate.of(1947, 9, 21));
		Autor autor2 = new Autor("Peter Straub", "Estados Unidos", LocalDate.of(1943, 3, 2));
		Libro libro1 = new Libro("El Talisman", LocalDate.of(2001, 9, 15),"37557779", "Random House");
		libro1.addAutor(autor1);
		libro1.addAutor(autor2);
		
		Libro libro2 = new Libro ("La Milla Verde", LocalDate.of(1996, 9, 1), "451933028", "Penguin Signet");
		libro2.addAutor(autor1);
		
		Libro libro3 = new Libro("El hobbit", LocalDate.of(1937, 9, 21), "618290307", "Houghton Miffin");
		Autor autor3 = new Autor("J.R.R. Tolkien", "Reino Unido", LocalDate.of(1892, 3, 2), LocalDate.of(1973, 9, 2));
		libro3.addAutor(autor3);
				
		System.out.println(libro1);
		System.out.println(libro2);
		System.out.println(libro3);
	}

}
