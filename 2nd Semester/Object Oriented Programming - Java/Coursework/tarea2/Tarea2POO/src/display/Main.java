package display;

import java.util.*;

import logic.Client;
import logic.Ticket;

public class Main {
    public static void main(String[] args) {
        Map<String, Client> clients = new HashMap<>();
        Queue<String> ticketQueue = new ArrayDeque<>();
        List<String> ticketHistorial = new ArrayList<>();

        boolean run = true;
        while(run){
            System.out.println();
            System.out.println("Clientes registrados:");
            System.out.println(clients.toString());
            System.out.println("Cola de atencion:");
            System.out.println(ticketQueue.toString());
            System.out.println("Historial:");
            System.out.println(ticketHistorial.toString());

            System.out.println("Elija alguna de las opciones escribiendo el numero de la opcion.");
            System.out.println("Opciones:");
            System.out.println("1. Agregar Cliente.");
            System.out.println("2. Agregar Tiquete a la Cola.");
            System.out.println("3. Atender Siguiente Tiquete de la Cola.");
            System.out.println("4. Descartar Siguiente Tiquete de la Cola.");
            System.out.println("5. Limpiar hitorial de tiquetes atendidos.");
            System.out.println("6. Salir.");

            Scanner reader = new Scanner(System.in);
            String option = reader.nextLine();


            switch (option) {

                case "1" -> {
                    //Anadir cliente

                    boolean addingClient = true;
                    while (addingClient) {
                        System.out.println("Escriba el ID del nuevo cliente: ");
                        String clientId = reader.nextLine();
                        if (clients.containsKey(clientId)) {
                            System.out.println("Cliente ya existe: " + clientId + " = " + clients.get(clientId));
                            System.out.println();

                            System.out.println("Desea intentar de nuevo o ya no desea agregar un nuevo cliente?");
                            System.out.println("Elija alguna de la siguientes 2 opciones:");
                            System.out.println("1. Intentar de nuevo.");
                            System.out.println("2. Ya no quiero agregar un nuevo cliente.");

                            option = reader.nextLine();

                            if (option.equals("2")) {
                                addingClient = false;
                            }

                        } else {
                            System.out.println("Escriba el nombre del nuevo cliente: ");
                            String clientName = reader.nextLine();

                            try {
                                Client client = new Client(clientId, clientName);
                                clients.put(clientId, client);
                                addingClient = false;
                            } catch (Exception e) {
                                System.out.println(e);
                                System.out.println();

                                System.out.println("Desea intentar de nuevo o ya no desea agregar un nuevo cliente?");
                                System.out.println("Elija alguna de la siguientes 2 opciones:");
                                System.out.println("1. Intentar de nuevo.");
                                System.out.println("2. Ya no quiero agregar un nuevo cliente.");

                                option = reader.nextLine();

                                if (option.equals("2")) {
                                    addingClient = false;
                                }
                            }
                        }
                    }
                }

                case "2" -> {
                    //Asignar Tiquete

                    boolean assigningTicket = true;
                    while (assigningTicket) {
                        System.out.println("Escriba el ID del cliente al que se le asignara el tiquete: ");
                        String clientId = reader.nextLine();
                        if (clients.containsKey(clientId)) {
                            try {
                                Ticket ticket = new Ticket(clientId);
                                ticketQueue.add(ticket.toString());
                                System.out.println("Tiquete agregado a la lista con exito. ");
                                System.out.println();
                                assigningTicket = false;
                            } catch (Exception e) {
                                System.out.println(e);
                                System.out.println();

                                System.out.println("Desea intentar de nuevo o ya no quiere asignar el tiquete?");
                                System.out.println("Elija alguna de la siguientes 2 opciones:");
                                System.out.println("1. Intentar de nuevo");
                                System.out.println("2. Ya no quiero asignar el tiquete.");

                                option = reader.nextLine();

                                if (option.equals("2")) {
                                    assigningTicket = false;
                                }
                            }
                        } else {
                            System.out.println("Cliente no existe.");
                            System.out.println();

                            System.out.println("Desea intentar de nuevo o ya no quiere asignar el tiquete?");
                            System.out.println("Elija alguna de la siguientes 2 opciones:");
                            System.out.println("1. Intentar de nuevo");
                            System.out.println("2. Ya no quiero asignar el tiquete.");

                            option = reader.nextLine();

                            if (option.equals("2")) {
                                assigningTicket = false;
                            }
                        }
                    }
                }

                case "3" -> {
                    //Atender tiquete

                    if (ticketQueue.isEmpty()) {
                        System.out.println();
                        System.out.println("No hay tiquetes por atender en la cola. ");
                        System.out.println();
                    } else {
                        String ticket = ticketQueue.remove();
                        System.out.println();
                        System.out.println("Tiquete atendido: " + ticket);
                        System.out.println();
                        ticketHistorial.add(ticket);
                    }
                }

                case "4" -> {
                    // Eliminar tiquete

                    if (ticketQueue.isEmpty()) {
                        System.out.println();
                        System.out.println("No hay tiquetes en la cola. ");
                        System.out.println();
                    } else {
                        String ticket = ticketQueue.remove();
                        System.out.println();
                        System.out.println("Tiquete eliminado de la lista: " + ticket);
                        System.out.println();
                    }
                }

                case "5" -> {
                    //Eliminar historial

                    ticketHistorial.clear();
                    System.out.println();
                    System.out.println("Historial de tiquetes atendidos eliminado.");
                    System.out.println();
                }

                case "6" -> {
                    //Salir

                    run = false;

                    System.out.println();
                    System.out.println("Gracias por usar el programa.");
                }

                case null, default -> {
                    System.out.println();
                    System.out.println("Elija alguna de las opciones indicadas.");
                    System.out.println();
                }
            }
        }
    }
}