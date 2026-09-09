package display;

import logic.Compania;
import logic.Empleado;

public class EjemploCompaniaEmpleado {
	
	public static void main(String[] args) {
		try {
			Compania compania1 = new Compania("PIPASA", "Heredia");
			compania1.contratar("3-5555-6666", "Claudio Gallo");
			compania1.contratar("6-7766-1122", "Cornelio Rooster");
			Empleado empleado1 = new Empleado("5-6666-5543", "Ana Gallega");
			compania1.contratar(empleado1);
			System.out.println(compania1);
			System.out.println(empleado1);
			compania1.despedir(empleado1.getCedula());
			System.out.println(compania1);
			System.out.println(empleado1);
		}
		catch (Exception e) {
			System.out.println(e);
		}
	}
}
