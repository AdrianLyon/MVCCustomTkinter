import customtkinter as ctk
from controllers.login_controller import LoginController

class App(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.title("CustomTkinter MVC Example")
        self.geometry("900x600")

        self.container = ctk.CTkFrame(self)
        self.container.pack(fill="both", expand=True)

        self.show_frame(LoginController)

    def show_frame(self, ControllerClass):
        for widget in self.container.winfo_children():
            widget.destroy()
        
        frame = ControllerClass(self.container, self)
        frame.pack(fill="both", expand=True)

if __name__ == "__main__":
    app = App()
    app.mainloop()
