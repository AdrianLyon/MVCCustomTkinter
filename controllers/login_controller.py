from views.login_view import LoginView
from models.user_model import UserModel

class LoginController(LoginView):
    def __init__(self, master, app):
        super().__init__(master, app)

    def check_login(self):
        username = self.username_entry.get()
        password = self.password_entry.get()

        # Usar el modelo para autenticar al usuario
        if UserModel.authenticate(username, password):
            from controllers.dashboard_controller import DashboardController
            self.app.show_frame(DashboardController)
        else:
            self.show_error("Credenciales incorrectas")
