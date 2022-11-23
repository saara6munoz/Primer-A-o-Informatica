package dao;
import modelo.Libro;
import java.util.List;

/**
 *
 * @author smunoz
 */
//Se define la "plantilla" de metodos tipo CRUD que va a implementar del DAO 
public interface LibroDAO {
    List<Libro> getAllLibros();
    Libro getLibroById(int idLibro);
    boolean agregarLibro(Libro libro);
    boolean borrarLibro(int idLibro);
    boolean actualizarLibro(Libro libro);
}
