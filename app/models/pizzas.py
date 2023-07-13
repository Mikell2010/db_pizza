import os
from app.config.mysqlconnection import connectToMySQL
from flask import flash


class Pizza:

    def __init__(self, data):
        self.id = data.get('id', 0)
        self.size = data.get('size')
        self.crust = data.get('crust')
        self.cantidad = data.get('cantidad')
        self.descripcion_pizza = data.get('descripcion_pizza')
        self.nombre_pizza = data.get('nombre_pizza')
        self.precio = data.get('precio')
        self.created_at = data.get('created_at', '')
        self.updated_at = data.get('updated_at', '')

    @classmethod
    def get_all(cls):  # todas las pizzas
        sql = """
        SELECT id, size, crust, cantidad, descripcion_pizza, nombre_pizza, precio, created_at, updated_at FROM pizzas;
        """
        result = connectToMySQL(os.getenv("BASE_DE_DATOS")).query_db(sql)

        return result

    @classmethod
    def save(cls, data):
        sql = """
        INSERT INTO pizzas (size, crust, cantidad, descripcion_pizza, nombre_pizza, precio, created_at, updated_at) VALUES (%(size)s, %(crust)s, %(cantidad)s, %(descripcion_pizza)s, %(nombre_pizza)s, %(precio)s, NOW(), NOW());
        """
        result = connectToMySQL(os.getenv("BASE_DE_DATOS")).query_db(sql, data)

        return cls.get(result)

    @classmethod
    def get(cls, id):
        sql = """
        SELECT id, size, crust, cantidad, descripcion_pizza, nombre_pizza, precio, created_at, updated_at FROM pizzas where id = %(id)s;
        """
        data = {
            'id': id
        }
        result = connectToMySQL(os.getenv("BASE_DE_DATOS")).query_db(sql, data)

        return (result[0])

    @classmethod
    def delete(cls, id):
        sql = """
        DELETE FROM pizzas where id = %(id)s;
        """
        data = {
            'id': id
        }
        result = connectToMySQL(os.getenv("BASE_DE_DATOS")).query_db(sql, data)

        return result

    @classmethod
    def update(cls, data):
        sql = """
        UPDATE pizzas SET size = %(size)s, crust = %(crust)s, cantidad = %(cantidad)s, descripcion_pizza = %(descripcion_pizza)s, nombre_pizza = %(nombre_pizza)s, precio = %(precio)s, updated_at = NOW() where id = %(id)s;
        """
        result = connectToMySQL(os.getenv("BASE_DE_DATOS")).query_db(sql, data)

        return cls.get(data['id'])

    @classmethod
    def get_by_name(cls, nombre_pizza):
        sql = """
        SELECT id, size, crust, cantidad, descripcion_pizza, nombre_pizza, precio, created_at, updated_at FROM pizzas where nombre_pizza = %(nombre_pizza)s;
        """
        data = {
            'nombre_pizza': nombre_pizza
        }
        result = connectToMySQL(os.getenv("BASE_DE_DATOS")).query_db(sql, data)

        if result:
            return cls(result[0])

        return None

    @classmethod
    def get_random(cls):
        sql = """
        SELECT id, size, crust, cantidad, descripcion_pizza, nombre_pizza, precio, created_at, updated_at FROM pizzas ORDER BY RAND() LIMIT 1;
        """
        result = connectToMySQL(os.getenv("BASE_DE_DATOS")).query_db(sql)

        if result:
            return result[0]
            # return cls(result[0])

        return None
