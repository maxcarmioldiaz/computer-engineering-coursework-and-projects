package logic;

import java.time.LocalDate;

public class Autor {
private String name;
private String country;
private LocalDate fechaNac;
private LocalDate fechaFac;

public Autor(String name, String country, LocalDate fechaNac, LocalDate fechaFac) {
	super();
	this.name = name;
	this.country = country;
	this.fechaNac = fechaNac;
	this.fechaFac = fechaFac;
}

public Autor(String name, String country, LocalDate fechaNac) {
	super();
	this.name = name;
	this.country = country;
	this.fechaNac = fechaNac;
	this.fechaFac = null;
}

public String getName() {
	return name;
}

public void setName(String name) {
	this.name = name;
}

public String getCountry() {
	return country;
}

public void setCountry(String country) {
	this.country = country;
}

public LocalDate getFechaNac() {
	return fechaNac;
}

public void setFechaNac(LocalDate fechaNac) {
	this.fechaNac = fechaNac;
}

public LocalDate getFechaFac() {
	return fechaFac;
}

public void setFechaFac(LocalDate fechaFac) {
	this.fechaFac = fechaFac;
}

public String toString() {
	String myString = "Autor(" + name + ", " + country + ")";
	return myString;
}

}
