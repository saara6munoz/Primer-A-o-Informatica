/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package ventascooter;

import java.util.ArrayList;

/**
 *
 * @author
 */
public class Empresa {

    private ArrayList<Empleado> listaEmpleados;

    public Empresa() {
        listaEmpleados = new ArrayList<Empleado>();
    }

    //agregar
    public boolean agregar(Empleado emple) {
        return listaEmpleados.add(emple);
    }

    //buscar
    public boolean buscarEmpleado(String rut) {
        for (Empleado emple : listaEmpleados) {
            if (emple.getRut().equals(rut)) {
                return true;
            }
        }
        return false;
    }

    //listar empleados
    public void listarEmpleados() {
        for (Empleado emple : listaEmpleados) {
            System.out.println(emple.toString());
        }
    }

    //eliminar empleado
    public boolean eliminarEmpleado(String rut) {
        for (Empleado emple : listaEmpleados) {
            if (emple.getRut().equals(rut)) {
                listaEmpleados.remove(emple);
                return true;
            }
        }
        return false;
    }

    //liste todos los ejecutivos
    public void listarEmpleadosEjecutivos() {
        for (Empleado emple : listaEmpleados) {
            if (emple.getPuesto().getNombrePuesto().equals("ejecutivo")) {
                System.out.println(emple.toString());
            }
        }
    }

    //método que modifique la edad de un empleado
    public void modificarEdadEmpleado(int nuevaEdad, String rut) {
        for (Empleado emple : listaEmpleados) {
            if (emple.getRut().equals(rut)) {
                emple.setEdad(nuevaEdad);
            }
        }
    }

}
