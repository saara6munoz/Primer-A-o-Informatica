/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package ventascooter;

/**
 *
 * @author
 */
public class Empleado {

    private String rut, nombreEmpleado, genero;
    private int acno, edad;
    private Puesto puesto;

    public Empleado() {
        puesto = new Puesto();
    }

    public Empleado(String rut, String nombreEmpleado, String genero, int acno, int edad, Puesto puesto) {
        this.rut = rut;
        this.nombreEmpleado = nombreEmpleado;
        this.genero = genero;
        this.acno = acno;
        this.edad = edad;
        this.puesto = puesto;
    }

    public String getRut() {
        return rut;
    }

    public void setRut(String rut) {
        this.rut = rut;
    }

    public String getNombreEmpleado() {
        return nombreEmpleado;
    }

    public void setNombreEmpleado(String nombreEmpleado) {
        this.nombreEmpleado = nombreEmpleado;
    }

    public String getGenero() {
        return genero;
    }

    public void setGenero(String genero) {
        this.genero = genero;
    }

    public int getAcno() {
        return acno;
    }

    public void setAcno(int acno) {
        this.acno = acno;
    }

    public int getEdad() {
        return edad;
    }

    public void setEdad(int edad) {
        this.edad = edad;
    }

    public Puesto getPuesto() {
        return puesto;
    }

    public void setPuesto(Puesto puesto) {
        this.puesto = puesto;
    }

    @Override
    public String toString() {
        return "Empleado" + ", rut= " + rut + ", nombre= " + nombreEmpleado + ", genero= " + genero + ", acno= " + acno + ", edad= " + edad + ", puesto= " + puesto;
    }

    //valida edad mínimo 18 años
    public boolean validarEdad(int edad) {
        if (edad >= 18) {
            return true;
        } else {
            return false;
        }
    }

    //valida género F o M
    public boolean validarGenero(char genero) {
        if (genero == 'F' || genero == 'M') {
            return true;
        } else {
            return false;
        }
    }

    //valida nombre que no venga vacío
    public boolean validarNombre(String nombre) {
        if (nombre.isEmpty()) {
            return false;
        } else {
            return true;
        }
    }

}
