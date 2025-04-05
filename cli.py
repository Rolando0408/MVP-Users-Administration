from dao.user_dao import UserDAO
from utils.validators import Validator
import logging
import os

logging.basicConfig(level=logging.INFO)

def main():
    while True:
        os.system('cls')
        print("\n--- MVP Gestión de Usuarios ---")
        print("1. Crear Usuario")
        print("2. Listar Usuarios")
        print("3. Salir")
        
        opcion = input("Seleccione una opción: ")
        
        if opcion == "1":
            os.system('cls')
            print("\n--- Crear Usuario ---")
            username = input("Ingrese el nombre de usuario: ")
            password = input("Ingrese la contraseña: ")
            email = input("Ingrese el correo electrónico: ")
            
            if Validator.is_valid_input(username, password, email) and Validator.is_valid_email(email):
                
                try:
                    os.system('cls')
                    UserDAO.create_user(username, password, email)
                    print("Usuario creado correctamente.")
                    input("Presione Enter para continuar.")
                except Exception as e:
                    os.system('cls')
                    print(f"Error al crear el usuario: {e}")
                    input("Presione Enter para continuar.")
            else:
                os.system('cls')
                print("Datos inválidos. Por favor, verifique.")
                input("Presione Enter para continuar.")
                
        elif opcion == "2":
            try:
                os.system('cls')
                users = UserDAO.get_users()
                print("\n--- Lista de Usuarios ---")
                for user in users:
                    print(f"ID: {user[0]}, Nombre: {user[1]}, Correo: {user[3]}")
                input("Presione Enter para continuar.")
            except Exception as e:
                os.system('cls')
                print(f"Error al listar los usuarios: {e}")
                input("Presione Enter para continuar.")
                
        elif opcion == "3":
            os.system('cls')
            print("Saliendo...")
            input("Presione Enter para continuar.")
            break
        
        else:
            os.system('cls')
            print("Opción no válida. Intente de nuevo.")
            input("Presione Enter para continuar.")
            
if __name__ == "__main__":
    main()
