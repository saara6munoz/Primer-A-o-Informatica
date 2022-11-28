package bd;

import java.sql.Connection;
import java.sql.DriverManager;
import java.sql.SQLException;

//Clase generica que prueba la conexion
public class Conexion {

    public Connection obtenerConexion() {
        Connection connection = null;
        try {
            Class.forName("com.mysql.jdbc.Driver");
            connection = DriverManager.getConnection("jdbc:mysql://localhost:3306/libreria", "root", "root");
            System.out.println("Conexión exitosa");
        } catch (SQLException e) {
            System.out.println("Error de conexión" + e.getMessage());
        } catch (Exception ex) {
            System.out.println(ex.getMessage());
        }
        return connection;
    }
}
