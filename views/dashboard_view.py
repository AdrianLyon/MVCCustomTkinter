import customtkinter as ctk

class DashboardView(ctk.CTkFrame):
    def __init__(self, master, app):
        super().__init__(master)
        self.app = app

        # Sidebar (panel lateral)
        sidebar = ctk.CTkFrame(self, width=200, corner_radius=0)
        sidebar.pack(side="left", fill="y")

        ctk.CTkLabel(sidebar, text="CustomTkinter", font=("Arial", 16)).pack(pady=20)

        self.product_button = ctk.CTkButton(sidebar, text="Producto")
        self.product_button.pack(pady=10)

        self.category_button = ctk.CTkButton(sidebar, text="Categoría")
        self.category_button.pack(pady=10)

        self.provider_button = ctk.CTkButton(sidebar, text="Proveedor")
        self.provider_button.pack(pady=10)

        # Contenido central
        content_frame = ctk.CTkFrame(self)
        content_frame.pack(side="left", fill="both", expand=True, padx=20, pady=20)

        ctk.CTkLabel(content_frame, text="Bienvenido al Dashboard", font=("Arial", 20)).pack(pady=20)
