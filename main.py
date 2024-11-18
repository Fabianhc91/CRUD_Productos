import json

class Producto:
    def __init__(self, id, nombre, descripcion, precio, cantidad):
        self.id = id
        self.nombre = nombre
        self.descripcion = descripcion
        self.precio = precio
        self.cantidad = cantidad

    def to_dict(self):
        return {
            'id': self.id,
            'nombre': self.nombre,
            'descripcion': self.descripcion,
            'precio': self.precio,
            'cantidad': self.cantidad
        }

class ProductoNoEncontradoError(Exception):
    """Excepción personalizada cuando no se encuentra el producto."""
    pass

class CRUDProductos:
    def __init__(self, archivo):
        self.archivo = archivo
        self.productos = self.cargar_productos()

    def cargar_productos(self):
        try:
            with open(self.archivo, 'r') as f:
                return [Producto(**prod) for prod in json.load(f)]
        except FileNotFoundError:
            return []

    def guardar_productos(self):
        with open(self.archivo, 'w') as f:
            json.dump([prod.to_dict() for prod in self.productos], f, indent=4)

    def crear_producto(self, id, nombre, descripcion, precio, cantidad):
        producto = Producto(id, nombre, descripcion, precio, cantidad)
        self.productos.append(producto)
        self.guardar_productos()

    def leer_producto(self, id):
        for prod in self.productos:
            if prod.id == id:
                return prod.to_dict()
        return None

    def actualizar_producto(self, id, nombre=None, descripcion=None, precio=None, cantidad=None):
        producto = self.leer_producto(id)
        if producto is None:
            raise ProductoNoEncontradoError(f"Producto con id {id} no encontrado.")
        
        if nombre:
            producto['nombre'] = nombre
        if descripcion:
            producto['descripcion'] = descripcion
        if precio:
            producto['precio'] = precio
        if cantidad:
            producto['cantidad'] = cantidad
        
        self.guardar_productos()
        return producto

    def eliminar_producto(self, id):
        producto = self.leer_producto(id)
        if producto is None:
            raise ProductoNoEncontradoError(f"Producto con id {id} no encontrado.")
        
        self.productos = [prod for prod in self.productos if prod.id != id]
        self.guardar_productos()
        return True
