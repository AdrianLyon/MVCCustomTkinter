from views.dashboard_view import DashboardView

class DashboardController(DashboardView):
    def __init__(self, master, app):
        super().__init__(master, app)

        # Configurar los botones de la barra lateral para que cambien de vista
        self.product_button.configure(command=lambda: self.show_producto())
        self.category_button.configure(command=lambda: self.show_categoria())
        self.provider_button.configure(command=lambda: self.show_proveedor())

    def show_producto(self):
        from controllers.producto_controller import ProductoController
        self.app.show_frame(ProductoController)

    def show_categoria(self):
        from controllers.category_controller import CategoryController
        self.app.show_frame(CategoryController)

    def show_proveedor(self):
        from controllers.proveedor_controller import ProveedorController
        self.app.show_frame(ProveedorController)
