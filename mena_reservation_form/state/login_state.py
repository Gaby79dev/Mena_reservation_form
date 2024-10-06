import reflex as rx
import os
from dotenv import load_dotenv
from mena_reservation_form.state.navigation_state import NavigationState

load_dotenv()  # Carga el archivo .env

class LoginState(rx.State):
    email: str = ""
    password: str = ""
    error: str = ""
    is_authenticated: bool = False

    def set_email(self, email: str):
        self.email = email

    def set_password(self, password: str):
        self.password = password

    def login(self):
        login_password = os.getenv("LOGIN_PASSWORD")
        email_login = os.getenv("EMAIL_LOGIN")
        if self.email == email_login and self.password == login_password:
            self.is_authenticated = True
            return rx.redirect("/dashboard")
        else:
            self.error = "Credenciales inválidas"
            return rx.set_value("password", "")  # Limpiar el campo de contraseña

    def logout(self):
        self.is_authenticated = False
        return NavigationState.navigate_to_index