import customtkinter as ctk

class LoginView(ctk.CTkFrame):
    def __init__(self, master, app):
        super().__init__(master)
        self.app = app

        ctk.CTkLabel(self, text="Iniciar Sesión", font=("Arial", 20)).pack(pady=20)
        
        self.username_entry = ctk.CTkEntry(self, placeholder_text="Usuario")
        self.username_entry.pack(pady=10)

        self.password_entry = ctk.CTkEntry(self, placeholder_text="Contraseña", show="*")
        self.password_entry.pack(pady=10)

        login_button = ctk.CTkButton(self, text="Iniciar Sesión", command=self.check_login)
        login_button.pack(pady=20)

    def check_login(self):
        raise NotImplementedError("Debe ser implementado en el controlador.")

    def show_error(self, message):
        ctk.CTkLabel(self, text=message, text_color="red").pack(pady=5)
