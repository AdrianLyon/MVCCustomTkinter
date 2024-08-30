class UserModel:
    def __init__(self, username, password):
        self.username = username
        self.password = password

    @staticmethod
    def authenticate(username, password):
        # Aquí podrías agregar lógica para autenticar con una base de datos real
        return username == "admin" and password == "admin"
