package dao;

import bd.Conexion;
import java.sql.Connection;
import java.sql.PreparedStatement;
import java.sql.ResultSet;
import java.sql.SQLException;
import java.util.ArrayList;
import java.util.Date;
import java.util.List;
import modelo.Libro;

/**
 *
 * @author smunoz
 */
// deberia estar en otro package¿
//Implementa todo lo de la interfaz y le aplica logica (más vueltas que un trompo pero nah k hacer)
public class LibroDaoImpl implements LibroDAO{
    @Override
    public List<Libro> getAllLibros() {
        List<Libro> lista = new ArrayList<Libro>();

        try {
            Conexion conexion1 = new Conexion();
            Connection cnx = conexion1.obtenerConexion();

            String query = "SELECT idlibro, titulo, autor, publicacion, precio, disponible FROM libro order by titulo";
            PreparedStatement stmt = cnx.prepareStatement(query);

            ResultSet rs = stmt.executeQuery();

            while (rs.next()) {
                Libro libro = new Libro();
                libro.setIdLibro(rs.getInt("idlibro"));
                libro.setTitulo(rs.getString("titulo"));
                libro.setAutor(rs.getString("autor"));
                libro.setPublicacion(rs.getDate("publicacion"));
                libro.setPrecio(rs.getInt("precio"));
                libro.setDisponible(rs.getBoolean("disponible"));

                lista.add(libro);
            }
            rs.close();
            stmt.close();
            cnx.close();
        } catch (SQLException e) {
            System.out.println("Error SQL al listar libros" + e.getMessage());
        } catch (Exception e) {
            System.out.println("Error al listar libros" + e.getMessage());
        }
        return lista;
    }

    @Override
    public Libro getLibroById(int idLibro) {
        Libro libro = new Libro();
        try {
            Conexion conexion1 = new Conexion();
            Connection cnx = conexion1.obtenerConexion();

            String query = "SELECT idlibro, titulo, autor, publicacion, precio, disponible FROM libro WHERE idlibro=?";
            PreparedStatement stmt = cnx.prepareStatement(query);
            stmt.setInt(1, idLibro);

            ResultSet rs = stmt.executeQuery();

            if (rs.next()) {
                libro.setIdLibro(rs.getInt("idlibro"));
                libro.setTitulo(rs.getString("titulo"));
                libro.setAutor(rs.getString("autor"));
                libro.setPublicacion(rs.getDate("publicacion"));
                libro.setPrecio(rs.getInt("precio"));
                libro.setDisponible(rs.getBoolean("disponible"));
            }
            rs.close();
            stmt.close();
            cnx.close();
        } catch (SQLException e) {
            System.out.println("Error SQL al listar libro por id" + e.getMessage());
        } catch (Exception e) {
            System.out.println("Error al listar libro por id" + e.getMessage());
        }
        return libro;
    }

    @Override
    public boolean agregarLibro(Libro libro) {
                Date date;
        try {
            Conexion conexion1 = new Conexion();
            Connection cnx = conexion1.obtenerConexion();

            date = libro.getPublicacion();
            
            String query = "INSERT INTO libro(titulo, autor, publicacion, precio, disponible) VALUES (?,?,?,?,?)";
            PreparedStatement stmt = cnx.prepareStatement(query);
            stmt.setString(1, libro.getTitulo());
            stmt.setString(2, libro.getAutor());
            stmt.setDate(3, new java.sql.Date(date.getTime()));
            stmt.setInt(4, libro.getPrecio());
            stmt.setBoolean(5, libro.isDisponible());

            stmt.executeUpdate();
            stmt.close();
            cnx.close();
            return true;
        } catch (SQLException e) {
            System.out.println("Error SQL al agregar libro" + e.getMessage());
            return false;
        } catch (Exception e) {
            System.out.println("Error al agregar libro" + e.getMessage());
            return false;
        }
    }

    @Override
    public boolean borrarLibro(int idLibro) {
        try {
            Conexion conexion1 = new Conexion();
            Connection cnx = conexion1.obtenerConexion();

            String query = "DELETE FROM libro WHERE idlibro=?";
            PreparedStatement stmt = cnx.prepareStatement(query);
            stmt.setInt(1, idLibro);

            stmt.executeUpdate();
            stmt.close();
            cnx.close();
            return true;
        } catch (SQLException e) {
            System.out.println("Error SQL al eliminar libro" + e.getMessage());
            return false;
        } catch (Exception e) {
            System.out.println("Error al eliminar libro" + e.getMessage());
            return false;
        }
    }
    public boolean agregar(Libro libro) {
        Date date;
        try {
            Conexion conexion1 = new Conexion();
            Connection cnx = conexion1.obtenerConexion();

            date = libro.getPublicacion();
            
            String query = "INSERT INTO libro(titulo, autor, publicacion, precio, disponible) VALUES (?,?,?,?,?)";
            PreparedStatement stmt = cnx.prepareStatement(query);
            stmt.setString(1, libro.getTitulo());
            stmt.setString(2, libro.getAutor());
            stmt.setDate(3, new java.sql.Date(date.getTime()));
            stmt.setInt(4, libro.getPrecio());
            stmt.setBoolean(5, libro.isDisponible());

            stmt.executeUpdate();
            stmt.close();
            cnx.close();
            return true;
        } catch (SQLException e) {
            System.out.println("Error SQL al agregar libro" + e.getMessage());
            return false;
        } catch (Exception e) {
            System.out.println("Error al agregar libro" + e.getMessage());
            return false;
        }
    }

    @Override
    public boolean actualizarLibro(Libro libro) {
        try {
            Conexion conexion1 = new Conexion();
            Connection cnx = conexion1.obtenerConexion();

            String query = "UPDATE libro set titulo = ?, autor = ?, publicacion = ?, precio = ?, disponible = ? WHERE idlibro=?";
            PreparedStatement stmt = cnx.prepareStatement(query);
            stmt.setString(1, libro.getTitulo());
            stmt.setString(2, libro.getAutor());
            stmt.setDate(3, new java.sql.Date(libro.getPublicacion().getTime()));
            stmt.setInt(4, libro.getPrecio());
            stmt.setBoolean(5, libro.isDisponible());
            stmt.setInt(6, libro.getIdLibro());

            stmt.executeUpdate();
            stmt.close();
            cnx.close();
            return true;
        } catch (SQLException e) {
            System.out.println("Error SQL al actualizar libro" + e.getMessage());
            return false;
        } catch (Exception e) {
            System.out.println("Error al actualizar libro" + e.getMessage());
            return false;
        }
    }
 }
    

