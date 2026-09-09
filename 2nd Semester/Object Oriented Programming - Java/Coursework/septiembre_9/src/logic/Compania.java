package logic;

import java.util.Map;
import java.util.TreeMap;
import java.util.List;
import java.util.LinkedList;

public class Compania {
	private String nombre;
	private String ubicacion;
	private Map<String, Empleado> empleados;
	
	public Compania(String nombre, String ubicacion) {
		this.nombre = nombre;
		this.ubicacion = ubicacion;
		
		this.empleados = new TreeMap<String, Empleado>();
	}
	
	private boolean isEmpleado(String cedula) throws Exception {
		if (empleados == null)
			return false;
		return empleados.containsKey(cedula);
	}

	public String getNombre() {
		return nombre;
	}

	public void setNombre(String nombre) {
		this.nombre = nombre;
	}

	public String getUbicacion() {
		return ubicacion;
	}

	public void setUbicacion(String ubicacion) {
		this.ubicacion = ubicacion;
	}
	
	public void contratar(Empleado empleado) throws Exception {
		if (isEmpleado(empleado.getCedula()))
			throw new Exception("El empleado ya está contratado");
		empleados.put(empleado.getCedula(), empleado);
		empleado.setEmpleador(this);
	}
	
	public void contratar(String nombre, String cedula) throws Exception {
		if (isEmpleado(cedula))
			throw new Exception("El empleado ya está contratado");
		Empleado empleado = new Empleado(nombre, cedula, this);
		empleados.put(cedula, empleado);
	}
	
	public void despedir(String cedula) throws Exception {
		if (!isEmpleado(cedula))
			throw new Exception("El empleado no existe");
		Empleado e = empleados.remove(cedula);
		e.setEmpleador(null);
	}
	
	public List<Empleado> getEmpleados() {
		List<Empleado> lista = new LinkedList<Empleado>();
		for (Map.Entry<String, Empleado> entry : empleados.entrySet()) {
			lista.add(entry.getValue());
		}
		return lista;
	}
	
	public String toString() {
		String myString = "Compañia(" + nombre + ", " + ubicacion + ", Empleados(";
		for (Empleado e : empleados.values()) {
			myString += e.toString() + '\n';
		}
		myString += ")";
		return myString;
	}
	
}
