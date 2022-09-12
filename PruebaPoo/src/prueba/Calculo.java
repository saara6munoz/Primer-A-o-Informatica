package prueba;

/**
 *
 * @author spich
 */
public class Calculo {
    
    public float horasNoTrabajadas(float sueldoBruto, int hora){
    float dctoHoraNoTrabajada = Math.round(((sueldoBruto / 180) * (180-hora)));
    return dctoHoraNoTrabajada;
    }
    public float sueldoImponible(float sueldoBruto, int dctoHoraNoTrabajada){
    float sueldoImponible = Math.round(sueldoBruto - dctoHoraNoTrabajada);
    return sueldoImponible;
    }
    public float dctoPrevisionales(float sueldoImponible){
    float dctoPrevisionales = Math.round((float) (sueldoImponible * 0.20));
    return dctoPrevisionales;
    }
    public float sueldoLiquido(float sueldoImponible, float dctoPrevisionales){
    float sueldoLiquido = Math.round(sueldoImponible - dctoPrevisionales);
    return sueldoLiquido;
    }
    
}

  