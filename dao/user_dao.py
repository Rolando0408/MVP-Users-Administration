from config.database import ConfigDatabase
from utils.validators import Validator  # Importa el validador
import logging

logger = logging.getLogger(__name__)

class UserDAO:
    @staticmethod
    def create_user(username, password, email):
        """
        Método para crear un usuario. Valida los datos antes de llamar al procedimiento almacenado.
        """
        # Validar datos de entrada
        if not username.strip() or not password.strip() or not email.strip():
            raise ValueError("Los campos no pueden estar vacíos.")
        if not Validator.is_valid_email(email):
            raise ValueError("El correo electrónico no es válido.")

        # Se obtiene el pool de conexiones de la base de datos
        pool = ConfigDatabase.get_connection_pool()
        connection = pool.connection()
        try:
            with connection.cursor() as cursor:
                connection.begin()
                # Llamada al procedimiento almacenado de la base de datos para insertar usuario
                sql = "CALL InsertUsuario(%s, %s, %s)"
                # Se ejecuta la consulta SQL con los parámetros
                cursor.execute(sql, (username, password, email))
                connection.commit()
                logger.info(f"Usuario creado correctamente: {username} - {email}")
                return True
        except Exception as e:
            logger.error(f"Error al crear el usuario: {e}")
            connection.rollback()
            raise
        finally:
            connection.close()
            
    @staticmethod
    def get_users():#Metodo para obtener todos los usuarios
        # Se obtiene el pool de conexiones de la base de datos
        pool= ConfigDatabase.get_connection_pool()
        connection = pool.connection()
        try:
            with connection.cursor() as cursor:
                # Se ejecuta la consulta SQL 
                cursor.execute("select * from usuarios")
                # Se obtienen todos los resultados
                return cursor.fetchall()
        finally:
            connection.close()
