import re
import os
from app.config.mysqlconnection import connectToMySQL
from flask import flash

SEGURA_REGEX = re.compile(r'^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*?&#])[A-Za-z\d@$!%*?&#]{8,}$')

class Usuario:

    def __init__(self, data):
        self.id = data.get('id', 0)
        self.nombre = data.get('nombre')
        self.apellido = data.get('apellido')
        self.email = data['email']
        self.direccion = data.get('direccion')
        self.ciudad = data.get('ciudad')
        self.region = data.get('region')
        self.password = data['password']
        self.created_at = data.get('created_at', '')
        self.updated_at = data.get('updated_at', '')

    @staticmethod
    def validar(data):

        todo_ok = True

        if not SEGURA_REGEX.match(data['password']):
            flash("Tu contraseña debe tener 8 caracteres, una mayuscula, minuscula, numero y caracter especial", "danger")
            todo_ok = False

        return todo_ok

    @classmethod
    def get_all(cls):
        todos_los_datos = []

        sql = """
        SELECT id, nombre, apellido, email, direccion, ciudad, region, password, created_at, updated_at FROM usuarios;
        """
        result = connectToMySQL(os.getenv("BASE_DE_DATOS")).query_db(sql);
        for fila in result:
            instancia = cls(fila)
            todos_los_datos.append(instancia)
        return todos_los_datos

    def crear(self):
        sql = f"INSERT INTO usuarios (nombre, apellido, email, direccion, ciudad, region, password ,created_at,updated_at) VALUES (%(nombre)s, %(apellido)s, %(email)s, %(direccion)s, %(ciudad)s, %(region), %(password)s,NOW(),NOW());"
        data = {
            'email': self.email,
            'password': self.password,
            'nombre': self.nombre,
            'apellido': self.apellido,
            'direccion': self.direccion,
            'ciudad': self.ciudad,
            'region': self.region
        }
        self.id = connectToMySQL(os.getenv("BASE_DE_DATOS")).query_db(sql, data)
        return self

    @classmethod
    def save(cls, data):
        sql = """
        INSERT INTO usuarios (nombre, apellido, email, direccion, ciudad, region, password ,created_at,updated_at) 
        VALUES (%(nombre)s, %(apellido)s, %(email)s, %(direccion)s, %(ciudad)s, %(region)s, %(password)s,NOW(),NOW());
        """
        
        id = connectToMySQL(os.getenv("BASE_DE_DATOS")).query_db(sql, data)
        print("ID:", id)
        resultado = None
        if id:
            resultado = cls.get(id)
        return resultado

    @classmethod
    def get(cls, id):
        sql = """
        SELECT id, nombre, apellido, email, direccion, ciudad, region, password, created_at, updated_at FROM usuarios where id = %(id)s;
        """
        data = {
            'id': id
        }
        result = connectToMySQL(os.getenv("BASE_DE_DATOS")).query_db(sql, data);
        
        return cls(result[0])

    @classmethod
    def get_by_email(cls, email):
        sql = """
        SELECT id, nombre, apellido, email, direccion, ciudad, region, password, created_at, updated_at FROM usuarios where email = %(email)s;
        """
        data = {
            'email': email
        }
        result = connectToMySQL(os.getenv("BASE_DE_DATOS")).query_db(sql, data);
        print("Valor de email:", email)

        if result:
            return cls(result[0])

        return None
    
    @classmethod
    def delete(cls, id):
        sql = """
        DELETE FROM usuarios where id = %(id)s;
        """
        data = {
            'id': id
        }
        result = connectToMySQL(os.getenv("BASE_DE_DATOS")).query_db(sql, data);

        return result

    def actualizar(self):

        sql = """
            UPDATE usuarios
                SET
                nombre = %(nombre)s,
                apellido = %(apellido)s,
                email = %(email)s,
                direccion = %(direccion)s,
                ciudad = %(ciudad)s,
                region = %(region)s,
                password = %(password)s,
                updated_at = NOW()
                WHERE id = %(id)s;
            """

        data = {
            'nombre': self.nombre,
            'apellido': self.apellido,
            'email': self.email,
            'direccion': self.direccion,
            'ciudad': self.ciudad,
            'region': self.region,
            'password': self.password,
            'id': self.id
        }
        self.id = connectToMySQL(os.getenv("BASE_DE_DATOS")).query_db(sql, data)
        return self

