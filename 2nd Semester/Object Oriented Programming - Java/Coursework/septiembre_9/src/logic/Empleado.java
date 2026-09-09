package logic;

public class Empleado {
	private String nombre;
	private String cedula;
	private Compania empleador;
	
	public Empleado(String nombre, String cedula) {
		this.nombre = nombre;
		this.cedula = cedula;
	}
	
	public Empleado(String nombre, String cedula, Compania empleador) {
		this.nombre = nombre;
		this.cedula = cedula;
		this.empleador = empleador;
	}

	public String getNombre() {
		return nombre;
	}

	public void setNombre(String nombre) {
		this.nombre = nombre;
	}

	public String getCedula() {
		return cedula;
	}

	public void setCedula(String cedula) {
		this.cedula = cedula;
	}

	public Compania getEmpleador() {
		return empleador;
	}

	public void setEmpleador(Compania empleador) {
		this.empleador = empleador;
	}
	
	public String toString() {
		if (empleador == null) {
			String myString = "Empleado(" + nombre + ", " + cedula + ", SIN EMPLEADOR)";
			return myString;
		}
		String myString = "Empleado(" + nombre + ", " + cedula + ", " + empleador.getNombre() + ")";
		return myString;
	}
}
