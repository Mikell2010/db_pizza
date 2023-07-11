import os
from app.config.mysqlconnection import connectToMySQL
from flask import flash

class Topping:

    def __init__(self, data):
        self.id = data.get('id', 0)
        self.nombre = data.get('nombre')
        self.precio = data.get('precio')
        self.created_at = data.get('created_at', '')
        self.updated_at = data.get('updated_at', '')

    
    @classmethod
    def get_all(cls):
        todos_los_datos = []

        sql = """
        SELECT id, nombre, precio, created_at, updated_at FROM toppings;
        """
        result = connectToMySQL(os.getenv("BASE_DE_DATOS")).query_db(sql);
        for fila in result:
            instancia = cls(fila)
            todos_los_datos.append(instancia)
        return todos_los_datos
    
    def crear(self):
        sql = f"INSERT INTO toppings (nombre, precio, created_at, updated_at) VALUES (%(nombre)s, %(precio)s, NOW(), NOW());"
        data = {
            'nombre': self.nombre,
            'precio': self.precio
        }
        self.id = connectToMySQL(os.getenv("BASE_DE_DATOS")).query_db(sql, data)
        return self
    
    @classmethod
    def agregar_topping(cls, data):
        sql = """
        INSERT INTO toppings (nombre, precio, created_at, updated_at) 
        VALUES (%(nombre)s, %(precio)s, NOW(), NOW());
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
        SELECT id, nombre, precio, created_at, updated_at FROM toppings where id = %(id)s;
        """
        data = {
            'id': id
        }
        result = connectToMySQL(os.getenv("BASE_DE_DATOS")).query_db(sql, data);
        
        if len(result) > 0:
            return cls(result[0])
        return result
    
    @classmethod
    def actualizar(cls, data):
        sql = """
        UPDATE toppings SET nombre = %(nombre)s, precio = %(precio)s, updated_at = NOW() WHERE id = %(id)s;
        """
        return connectToMySQL(os.getenv("BASE_DE_DATOS")).query_db(sql, data)
    
    @classmethod
    def eliminar(cls, id):
        sql = """
        DELETE FROM toppings WHERE id = %(id)s;
        """
        data = {
            'id': id
        }
        return connectToMySQL(os.getenv("BASE_DE_DATOS")).query_db(sql, data)
    
    @staticmethod
    def validar(data):
        es_valido = True
        if len(data['nombre']) < 3:
            flash("El nombre debe tener al menos 3 caracteres", "nombre")
            es_valido = False
        if float(data['precio']) < 0:
            flash("El precio debe ser mayor a 0", "precio")
            es_valido = False
        return es_valido

    

