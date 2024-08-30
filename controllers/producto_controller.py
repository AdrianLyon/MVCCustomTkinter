from views.producto_view import ProductoView
from models.producto_model import ProductoModel

class ProductoController(ProductoView):
    def __init__(self, master, app):
        super().__init__(master, app)
        # Configurar el botón para regresar al Dashboard
        self.back_button.configure(command=lambda: self.go_back())
        self.load_productos()

    def load_productos(self):
        productos = ProductoModel.load_all()
        # Lógica para mostrar productos en la vista
        pass

    def go_back(self):
        from controllers.dashboard_controller import DashboardController
        self.app.show_frame(DashboardController)