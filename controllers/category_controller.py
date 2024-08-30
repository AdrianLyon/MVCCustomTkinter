from views.category_view import CategoryView

class CategoryController(CategoryView):
    def __init__(self, master, app):
        super().__init__(master, app)
        # Configurar el botón para regresar al Dashboard
        self.back_button.configure(command=lambda: self.go_back())

    def go_back(self):
        from controllers.dashboard_controller import DashboardController
        self.app.show_frame(DashboardController)
