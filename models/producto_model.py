class ProductoModel:
    def __init__(self, nombre, precio):
        self.nombre = nombre
        self.precio = precio

    # Método para guardar el producto en la base de datos
    def save(self):
        # Lógica para guardar el producto
        pass

    # Método para cargar productos de la base de datos
    @staticmethod
    def load_all():
        # Lógica para cargar productos
        return []

    # Método para encontrar un producto por ID
    @staticmethod
    def find_by_id(product_id):
        # Lógica para encontrar un producto
        return ProductoModel("Ejemplo", 0)