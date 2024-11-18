import unittest
from main import CRUDProductos, ProductoNoEncontradoError  # Asegúrate de que las rutas sean correctas

class TestCRUDProductos(unittest.TestCase):
    """
    Clase de pruebas unitarias para CRUDProductos.
    """
    def setUp(self):
        """
        Configuración inicial para cada prueba. 
        Crea una instancia de CRUDProductos utilizando un archivo JSON ficticio.
        """
        self.crud = CRUDProductos('productos_test.json')

    # Pruebas para la creación de productos
    def test_crear_producto(self):
        """
        Prueba para crear un producto nuevo y verificar que se guarda correctamente.
        """
        self.crud.crear_producto(1, 'Guitarra Acústica', 'color azul', 1500000, 10)
        producto = self.crud.leer_producto(1)
        self.assertIsNotNone(producto)
        self.assertEqual(producto['nombre'], 'Guitarra Acústica')
        self.assertEqual(producto['precio'], 1500000)

    # Pruebas para la lectura de productos
    def test_leer_producto(self):
        """
        Prueba para leer un producto existente.
        """
        self.crud.crear_producto(2, 'Piano', 'es de marca yamaha', 2000000, 20)
        producto = self.crud.leer_producto(2)
        self.assertIsNotNone(producto)
        self.assertEqual(producto['nombre'],'Piano')

    def test_leer_producto_no_existe(self):
        """
        Prueba para intentar leer un producto que no existe.
        """
        producto = self.crud.leer_producto(999)
        self.assertIsNone(producto)

    # Pruebas para la actualización de productos
    def test_actualizar_producto(self):
        """
        Prueba para actualizar un producto existente.
        """
        self.crud.crear_producto(3, 'Bajo', 'es electrico', 3000000, 30)
        self.crud.actualizar_producto(3, nombre='Bajo', precio=2500000)
        producto = self.crud.leer_producto(3)
        self.assertEqual(producto['nombre'], 'Bajo')
        self.assertEqual(producto['precio'], 3000000)

    def test_actualizar_producto_no_existe(self):
        """
        Prueba para intentar actualizar un producto que no existe.
        """
        with self.assertRaises(ProductoNoEncontradoError) as context:
            self.crud.actualizar_producto(999, nombre='Producto Inexistente')
        self.assertEqual(str(context.exception), 'Producto con id 999 no encontrado.')

        # Capturar el mensaje de la excepción
        mensaje_error = str(context.exception)
        print("Mensaje de error capturado:", mensaje_error)
        self.assertEqual(mensaje_error, 'Producto con id 999 no encontrado.')

    # Pruebas para la eliminación de productos
    def test_eliminar_producto(self):
        """
        Prueba para eliminar un producto existente.
        """
        self.crud.crear_producto(4, 'Batería', 'es de doble pedal', 5000000, 40)
        resultado = self.crud.eliminar_producto(4)
        self.assertTrue(resultado)
        producto = self.crud.leer_producto(4)
        self.assertIsNone(producto)

    def test_eliminar_producto_no_existe(self):
        """
        Prueba para intentar eliminar un producto que no existe.
        """
        with self.assertRaises(ProductoNoEncontradoError) as context:
            self.crud.eliminar_producto(999)
        self.assertEqual(str(context.exception), 'Producto con id 999 no encontrado.')

        # Capturar el mensaje de la excepción
        mensaje_error = str(context.exception)
        print("Mensaje de error capturado:", mensaje_error)
        self.assertEqual(mensaje_error, 'Producto con id 999 no encontrado.')

if __name__ == '__main__':
    unittest.main()
