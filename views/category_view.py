import customtkinter as ctk

class CategoryView(ctk.CTkFrame):
    def __init__(self, master, app):
        super().__init__(master)
        self.app = app

        ctk.CTkLabel(self, text="Gestión de Categorías", font=("Arial", 20)).pack(pady=20)

        # Botón para regresar al dashboard
        self.back_button = ctk.CTkButton(self, text="Regresar")
        self.back_button.pack(pady=20)

        # Aquí puedes añadir más widgets para gestionar categorías
