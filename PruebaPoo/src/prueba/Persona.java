package prueba;

import java.util.InputMismatchException;
/**
 *
 * @author spich
 */
public class Persona {
    private String nombres;
    private String apellidos;
    private int run;
    private String tipo;
    private char dv;
    private String fechaCon;
    private String fechaNac;
    private int tipoEncargo;
    private float sueldoBruto;
    private int hora;

    public int getHora() {
        return hora;
    }

    public void setHora(int hora) {
        this.hora = hora;
    }

    public float getSueldoBruto() {
        return sueldoBruto;
    }

    public void setSueldoBruto(float sueldoBruto) {
        this.sueldoBruto = sueldoBruto;
    }
        public String getNombres() {
        return nombres;
    }

    public void setNombres(String nombres) {
        this.nombres = nombres;
    }

    public String getApellidos() {
        return apellidos;
    }

    public void setApellidos(String apellidos) {
        this.apellidos = apellidos;
    }

    public Persona(String nombres, String apellidos, int run, String tipo, char dv, String fechaCon, String fechaNac, int tipoEncargo, float sueldoBruto, int hora) {
        this.nombres = nombres;
        this.apellidos = apellidos;
        this.run = run;
        this.tipo = tipo;
        this.dv = dv;
        this.fechaCon = fechaCon;
        this.fechaNac = fechaNac;
        this.tipoEncargo = tipoEncargo;
        this.sueldoBruto = sueldoBruto;
        this.hora = hora;
    }

    public Persona() {
    }

    public int getRun() {
        return run;
    }
    public String getTipo() {
        return tipo;
    }

    public void setTipo(String tipo) {
        this.tipo = tipo;
    }
    public void setRun(int run) {
        this.run = run;
    }

    public char getDv() {
        return dv;
    }

    public void setDv(char dv) {
        this.dv = dv;
    }

    public String getFechaNac() {
        return fechaNac;
    }

    public void setFechaNac(String fechaNac) {
        this.fechaNac = fechaNac;
    }

    public int getTipoEncargo() {
        return tipoEncargo;
    }

    public void setTipoEncargo(int tipoEncargo) {
        this.tipoEncargo = tipoEncargo;
    }

    public String getFechaCon() {
        return fechaCon;
    }

    public void setFechaCon(String fechaCon) {
        this.fechaCon = fechaCon;
    }
    
    public String cargo(int tipoCargo){
    String cargo = null;
    try{
        if (tipoCargo >= 5 || tipoCargo <= 0){
        System.out.println("Debe escoger un cargo válido");
    } else {
            switch(tipoCargo){
                case 1:
                    cargo = "Ayudante Contador";
                break;
                case 2:
                    cargo = "Contador General";
                break;
               case 3:
                    cargo = "Contador Tributario"; 
                break;
                case 4:
                    cargo = "Personal Administrativo";
                break;
                }
        }
    }catch(InputMismatchException ex){
        System.out.println("* Debe insertar un número *");
    }

        return cargo;
    }

    public void lista(Persona persona, Calculo calculo){
        System.out.println("- -   Datos empleado   - -");
        System.out.println("Nombre: "+persona.nombres+persona.apellidos);
        System.out.println("Fecha Nacimiento: "+persona.fechaNac);
        System.out.println("- Cargo -");
        System.out.println("Nombre: "+persona.tipo);
        System.out.println("Sueldo bruto: "+persona.sueldoBruto);
        System.out.println("Horas Laborales Trabajadas: "+persona.hora);
        System.out.println("Descuentos Horas No Trabajadas: "+calculo.horasNoTrabajadas( sueldoBruto, hora));
        System.out.println("Sueldo Imponible: "+calculo.sueldoImponible(sueldoBruto, (int) calculo.horasNoTrabajadas(sueldoBruto, hora)));
        System.out.println("Descuentos Previsionales: "+calculo.dctoPrevisionales(calculo.sueldoImponible(sueldoBruto, (int) calculo.horasNoTrabajadas(sueldoBruto, hora))));
        System.out.println("Sueldo Líquido: "+calculo.sueldoLiquido(calculo.sueldoImponible(sueldoBruto, (int) calculo.horasNoTrabajadas(sueldoBruto, hora)), calculo.dctoPrevisionales(calculo.sueldoImponible(sueldoBruto, (int) calculo.horasNoTrabajadas(sueldoBruto, hora)))));
        
    }                            
}
