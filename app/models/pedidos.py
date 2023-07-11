import os
from app.config.mysqlconnection import connectToMySQL
from flask import flash

class Pedido:

    def __init__(self, data):
        self.id = data.get('id', 0)
        self.usuario_id = data.get('usuario_id')
        self.pizza_id = data.get('pizza_id')
        self.fecha_pedido = data.get('fecha_pedido')
        self.methods = data.get('methods')
        self.toppings_elegidos = data.get('toppings_elegidos')
        self.precio = data.get('precio')
        self.created_at = data.get('created_at', '')
        self.updated_at = data.get('updated_at', '')

    @classmethod
    def get_all(cls):
        todos_los_datos = []

        sql = """
        SELECT id, usuario_id, pizza_id, fecha_pedido, methods, toppings_elegidos, precio, created_at, updated_at FROM pedidos;
        """
        result = connectToMySQL(os.getenv("BASE_DE_DATOS")).query_db(sql);
        for fila in result:
            instancia = cls(fila)
            todos_los_datos.append(instancia)
        return todos_los_datos
    
    def crear(self):
        sql = f"INSERT INTO pedidos (usuario_id, pizza_id, fecha_pedido, methods, toppings_elegidos, precio, created_at, updated_at) VALUES (%(usuario_id)s, %(pizza_id)s, %(fecha_pedido)s, %(methods)s, %(toppings_elegidos)s, %(precio)s, NOW(), NOW());"
        data = {
            'usuario_id': self.usuario_id,
            'pizza_id': self.pizza_id,
            'fecha_pedido': self.fecha_pedido,
            'methods': self.methods,
            'toppings_elegidos': self.toppings_elegidos,
            'precio': self.precio
        }
        self.id = connectToMySQL(os.getenv("BASE_DE_DATOS")).query_db(sql, data)
        return self
    
    @classmethod
    def agregar_pedido(cls, data):
        sql = """
        INSERT INTO pedidos (usuario_id, pizza_id, fecha_pedido, methods, toppings_elegidos, precio, created_at, updated_at) 
        VALUES (%(usuario_id)s, %(pizza_id)s, %(fecha_pedido)s, %(methods)s, %(toppings_elegidos)s, %(precio)s, NOW(), NOW());
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
        SELECT id, usuario_id, pizza_id, fecha_pedido, methods, toppings_elegidos, precio, created_at, updated_at FROM pedidos where id = %(id)s;
        """
        data = {
            'id': id
        }
        result = connectToMySQL(os.getenv("BASE_DE_DATOS")).query_db(sql, data);
        
        return cls(result[0]) if len(result) > 0 else None  
    
    
    
    @classmethod
    def get_by_usuario_id(cls, usuario_id):
        sql = """
        SELECT id, usuario_id, pizza_id, fecha_pedido, methods, toppings_elegidos, precio, created_at, updated_at FROM pedidos where usuario_id = %(usuario_id)s;
        """
        data = {
            'usuario_id': usuario_id
        }
        result = connectToMySQL(os.getenv("BASE_DE_DATOS")).query_db(sql, data);
        
        return cls(result[0]) if len(result) > 0 else None
    
    @classmethod
    def get_by_pizza_id(cls, pizza_id):
        sql = """
        SELECT id, usuario_id, pizza_id, fecha_pedido, methods, toppings_elegidos, precio, created_at, updated_at FROM pedidos where pizza_id = %(pizza_id)s;
        """
        data = {
            'pizza_id': pizza_id
        }
        result = connectToMySQL(os.getenv("BASE_DE_DATOS")).query_db(sql, data);
        
        return cls(result[0]) if len(result) > 0 else None
    
    @classmethod
    def get_by_fecha_pedido(cls, fecha_pedido):
        sql = """
        SELECT id, usuario_id, pizza_id, fecha_pedido, methods, toppings_elegidos, precio, created_at, updated_at FROM pedidos where fecha_pedido = %(fecha_pedido)s;
        """
        data = {
            'fecha_pedido': fecha_pedido
        }
        result = connectToMySQL(os.getenv("BASE_DE_DATOS")).query_db(sql, data);
        
        return cls(result[0]) if len(result) > 0 else None
    
    @classmethod
    def get_by_methods(cls, methods):
        sql = """
        SELECT id, usuario_id, pizza_id, fecha_pedido, methods, toppings_elegidos, precio, created_at, updated_at FROM pedidos where methods = %(methods)s;
        """
        data = {
            'methods': methods
        }
        result = connectToMySQL(os.getenv("BASE_DE_DATOS")).query_db(sql, data);
        
        return cls(result[0]) if len(result) > 0 else None
    
    @classmethod
    def get_by_toppings_elegidos(cls, toppings_elegidos):
        sql = """
        SELECT id, usuario_id, pizza_id, fecha_pedido, methods, toppings_elegidos, precio, created_at, updated_at FROM pedidos where toppings_elegidos = %(toppings_elegidos)s;
        """
        data = {
            'toppings_elegidos': toppings_elegidos
        }
        result = connectToMySQL(os.getenv("BASE_DE_DATOS")).query_db(sql, data);
        
        return cls(result[0]) if len(result) > 0 else None
    
    @classmethod
    def get_by_precio(cls, precio):
        sql = """
        SELECT id, usuario_id, pizza_id, fecha_pedido, methods, toppings_elegidos, precio, created_at, updated_at FROM pedidos where precio = %(precio)s;
        """
        data = {
            'precio': precio
        }
        result = connectToMySQL(os.getenv("BASE_DE_DATOS")).query_db(sql, data);
        
        return cls(result[0]) if len(result) > 0 else None
    
    @classmethod
    def get_by_created_at(cls, created_at):
        sql = """
        SELECT id, usuario_id, pizza_id, fecha_pedido, methods, toppings_elegidos, precio, created_at, updated_at FROM pedidos where created_at = %(created_at)s;
        """
        data = {
            'created_at': created_at
        }
        result = connectToMySQL(os.getenv("BASE_DE_DATOS")).query_db(sql, data);
        
        return cls(result[0]) if len(result) > 0 else None
    
    @classmethod
    def get_by_updated_at(cls, updated_at):
        sql = """
        SELECT id, usuario_id, pizza_id, fecha_pedido, methods, toppings_elegidos, precio, created_at, updated_at FROM pedidos where updated_at = %(updated_at)s;
        """
        data = {
            'updated_at': updated_at
        }
        result = connectToMySQL(os.getenv("BASE_DE_DATOS")).query_db(sql, data);
        
        return cls(result[0]) if len(result) > 0 else None
    
    


