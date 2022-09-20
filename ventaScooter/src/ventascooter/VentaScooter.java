package ventascooter;

import java.util.Scanner;

/**
 *
 * @author
 */
public class VentaScooter {

    /**
     * @param args the command line arguments
     */
    public static void main(String[] args) {
        Scanner leer = new Scanner(System.in);
        System.out.println("¿Cuántos empleados desea ingresar: ?");
        int cantidad = leer.nextInt();
        for(int i = 0; i < cantidad; i++){
            System.out.println("Confirme ingreso de nuevo empleado: s/n");
            char bucledec = leer.next().charAt(0);
            while(bucledec == 's'){
                System.out.println("Ingrese el puesto a asignar: ");
                System.out.println("(Gerente o Ejecutivo)");
                String puesto = leer.next();
                System.out.println("Añadir código de identificación númerico: ");
                int codigo = leer.nextInt();
                Puesto pueston = new Puesto(codigo, puesto);
                System.out.println("Ingrese el run del empleado: ");
                String rut = leer.next();
                System.out.println("Ingrese el nombre del empleado: ");
                String nombreEmpleado = leer.next();
                System.out.println("Ingrese el genero del empleado: ");
                String genero = leer.next();
                System.out.println("Ingrese los años de servicio:");
                int anio = leer.nextInt();
                System.out.println("Ingrese la edad del empleado: ");
                int edad = leer.nextInt();
                Empleado empleado1 = new Empleado(rut, nombreEmpleado, genero, anio, edad, pueston);
                Empresa empresa = new Empresa(); // crea la colección en el constructor

                //agregar empleado1
                if (empresa.buscarEmpleado(rut) == false) {
                    empresa.agregar(empleado1);
                    System.out.println("Se agregó empleado " + empleado1.getNombreEmpleado());
                } else {
                    System.out.println("Empleado existe");
                }
        
                //listar empleados
                empresa.listarEmpleados();
        
                //eliminar 
                System.out.println("Desea eliminar a un empleado? s/n: ");
                char decision = leer.next().charAt(0);
                if (decision == 's'){
                    System.out.println("Ingrese el rut del empleado que desea eliminar: ");
                    String run = leer.next();
                    if (empresa.eliminarEmpleado(run)) {
                        System.out.println("Se eliminó empleado " + empleado1.getNombreEmpleado());
                    } else {
                        System.out.println("No se eliminó empleado " + empleado1.getNombreEmpleado());
                    }
                }else{
                    System.out.println("No se eliminó empleado " + empleado1.getNombreEmpleado());}
            break;
            }
        }
    }  
}

   