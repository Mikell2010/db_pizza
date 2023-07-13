import os
from app.config.mysqlconnection import connectToMySQL
from flask import flash


class Favorito:
    def __init__(self, data):
        self.id = data.get('id', 0)
        self.usuario_id = data.get('usuario_id')
        self.pizza_id = data.get('pizza_id')
        self.created_at = data.get('created_at', '')
        self.updated_at = data.get('updated_at', '')

    @classmethod
    def get_all(cls):
        todos_los_datos = []

        sql = """
        SELECT id, usuario_id, pizza_id, created_at, updated_at FROM favoritos;
        """
        result = connectToMySQL(os.getenv("BASE_DE_DATOS")).query_db(sql)
        for fila in result:
            instancia = cls(fila)
            todos_los_datos.append(instancia)
        # return todos_los_datos
        return result

    def crear(self):
        sql = f"INSERT INTO favoritos (usuario_id, pizza_id, created_at, updated_at) VALUES (%(usuario_id)s, %(pizza_id)s, NOW(), NOW());"
        data = {
            'usuario_id': self.usuario_id,
            'pizza_id': self.pizza_id
        }
        self.id = connectToMySQL(
            os.getenv("BASE_DE_DATOS")).query_db(sql, data)
        return self

    @classmethod
    def agregar_favorito(cls, data):
        sql = """
        INSERT INTO favoritos (usuario_id, pizza_id, created_at, updated_at) 
        VALUES (%(usuario_id)s, %(pizza_id)s, NOW(), NOW());
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
        SELECT id, usuario_id, pizza_id, created_at, updated_at FROM favoritos where id = %(id)s;
        """
        data = {
            'id': id
        }
        result = connectToMySQL(os.getenv("BASE_DE_DATOS")).query_db(sql, data)

        return cls(result[0])

    # def get_by_usuario_id(cls, usuario_id): #esta de mas

    @classmethod
    def get_by_pizza_id(cls, pizza_id):
        sql = """
        SELECT id, usuario_id, pizza_id, created_at, updated_at FROM favoritos where pizza_id = %(pizza_id)s;
        """
        data = {
            'pizza_id': pizza_id
        }
        result = connectToMySQL(os.getenv("BASE_DE_DATOS")).query_db(sql, data)
        
        return (result[0])

    @classmethod
    def get_by_usuario_id_and_pizza_id(cls, usuario_id, pizza_id):
        sql = """
        SELECT id, usuario_id, pizza_id, created_at, updated_at FROM favoritos where usuario_id = %(usuario_id)s and pizza_id = %(pizza_id)s;
        """
        data = {
            'usuario_id': usuario_id,
            'pizza_id': pizza_id
        }
        result = connectToMySQL(os.getenv("BASE_DE_DATOS")).query_db(sql, data)

        return cls(result[0])

    @classmethod
    def delete(cls, id):
        sql = """
        DELETE FROM favoritos WHERE id = %(id)s;
        """
        data = {
            'id': id
        }
        return connectToMySQL(os.getenv("BASE_DE_DATOS")).query_db(sql, data)

    @classmethod
    def delete_by_usuario_id_and_pizza_id(cls, usuario_id, pizza_id):
        sql = """
        DELETE FROM favoritos WHERE usuario_id = %(usuario_id)s and pizza_id = %(pizza_id)s;
        """
        data = {
            'usuario_id': usuario_id,
            'pizza_id': pizza_id
        }
        return connectToMySQL(os.getenv("BASE_DE_DATOS")).query_db(sql, data)

    @classmethod
    def delete_by_pizza_id(cls, pizza_id):
        sql = """
        DELETE FROM favoritos WHERE pizza_id = %(pizza_id)s;
        """
        data = {
            'pizza_id': pizza_id
        }
        return connectToMySQL(os.getenv("BASE_DE_DATOS")).query_db(sql, data)

    @classmethod
    def delete_by_usuario_id_and_pizza_id(cls, usuario_id, pizza_id):
        sql = """
        DELETE FROM favoritos WHERE usuario_id = %(usuario_id)s and pizza_id = %(pizza_id)s;
        """
        data = {
            'usuario_id': usuario_id,
            'pizza_id': pizza_id
        }
        return connectToMySQL(os.getenv("BASE_DE_DATOS")).query_db(sql, data)

    @classmethod
    def actualizar(cls, data):
        sql = """
        UPDATE favoritos SET usuario_id = %(usuario_id)s, pizza_id = %(pizza_id)s, updated_at = NOW() WHERE id = %(id)s;
        """
        return connectToMySQL(os.getenv("BASE_DE_DATOS")).query_db(sql, data)

    @classmethod
    def actualizar_by_usuario_id_and_pizza_id(cls, data):
        sql = """
        UPDATE favoritos SET usuario_id = %(usuario_id)s, pizza_id = %(pizza_id)s, updated_at = NOW() WHERE usuario_id = %(usuario_id)s and pizza_id = %(pizza_id)s;
        """
        return connectToMySQL(os.getenv("BASE_DE_DATOS")).query_db(sql, data)

    @classmethod
    def actualizar_by_pizza_id(cls, data):
        sql = """
        UPDATE favoritos SET pizza_id = %(pizza_id)s, updated_at = NOW() WHERE pizza_id = %(pizza_id)s;
        """
        return connectToMySQL(os.getenv("BASE_DE_DATOS")).query_db(sql, data)
