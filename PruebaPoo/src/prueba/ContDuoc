package prueba;

import java.text.ParseException;
import java.util.InputMismatchException;
import java.util.Scanner;

/**
 *
 * @author spich
 */
public class ContDuoc {

    public static void main(String[] args) throws ParseException {
        Scanner leer = new Scanner(System.in);
        Persona persona = new Persona();
        Calculo calculo = new Calculo();
        int opcion, tipoEncargo;
        float sueldoBruto = 0;
        int run = 0;
        String fechaCon, nombres, apellidos;
        String tipo = null;
        Boolean verificar;
        Boolean salir = false;
        String fecha = null;
        int hora = 0;
        do{
            System.out.println("-- Menú --");
            System.out.println("1- Crear empleado con su tipo de cargo");
            System.out.println("2- Listar información del empleado y ejecutar métodos personalizados");
            System.out.println("3- Salir");
            try{
            System.out.println("Escoja una opción: ");
            opcion = leer.nextInt();
            switch(opcion){
                    case 1:
                        System.out.println("Ingrese su rut sin digito verificador ni guión:  ");
                        run = leer.nextInt();       
                        persona.setRun(run);
                        
                        System.out.println("Ingrese sus nombres: ");
                        nombres = leer.next();
                        persona.setNombres(nombres);
                        
                        System.out.println("Ingrese sus apellidos: ");
                        apellidos = leer.next();
                        persona.setApellidos(apellidos);
                        
                        System.out.println("Ingrese su fecha de nacimiento con el siguiente formato dd/mm/yyyy: ");
                        fecha = leer.next();
                        persona.setFechaNac(fecha);
                        
                        System.out.println("Escoja su tipo de cargo: ");
                        System.out.println("1- Ayudante Contador ");
                        System.out.println("2- Contador General");   
                        System.out.println("3- Contador Tributario");
                        System.out.println("4- Personal Administrativo");
                        tipoEncargo = leer.nextInt();
                        tipo = persona.cargo(tipoEncargo);
                        persona.setTipo(tipo);
                        while (tipo == null){ 
                            System.out.println("Escoja su tipo de cargo: ");
                            System.out.println("1- Ayudante Contador ");
                            System.out.println("2- Contador General");   
                            System.out.println("3- Contador Tributario");
                            System.out.println("4- Personal Administrativov");
                            tipoEncargo = leer.nextInt();
                            tipo = persona.cargo(tipoEncargo);
                            persona.setTipo(tipo);
                        }
                        
                        System.out.println("Ingrese su fecha de contratación con el formato dd/mm/yyyy: ");
                        fechaCon = leer.next();
                        persona.setFechaCon(fechaCon);
                        
                        System.out.println("Ingrese su sueldo bruto: ");
                        sueldoBruto = leer.nextInt();
                        persona.setSueldoBruto(sueldoBruto);
                        while (sueldoBruto <= 0){
                            System.out.println("Debe ingresar un sueldo válido");
                            System.out.println("Ingrese su sueldo bruto: ");
                            sueldoBruto = leer.nextInt();
                            persona.setSueldoBruto(sueldoBruto);
                        }
                        
                        System.out.println("Ingrese la cantidad de horas trabajadas: ");
                        hora = leer.nextInt();
                        persona.setHora(hora);
                        while(hora > 180 || hora <= 0){
                            System.out.println("Debe ingresar una cantidad de horas válidas");
                            System.out.println("Ingrese la cantidad de horas trabajadas: ");
                            hora = leer.nextInt();
                            persona.setHora(hora);
                        }
                        System.out.println("Presione una tecla para volver al menú");
                        leer.next();
                    break;
                    case 2: 
                        persona.lista(persona, calculo);
                        System.out.println("Presione una tecla para volver al menú");
                        leer.next();
                    break;
            }
            }catch(InputMismatchException ex){
                System.out.println("* Debe insertar un número *");
                leer.next();
                System.out.println("Presiona una tecla para volver al menú");
                leer.next();
            }
        }while(!salir);
    }
    
}
