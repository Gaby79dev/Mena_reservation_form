import reflex as rx
from mena_reservation_form.state.login_state import LoginState  # Asegúrate de importar LoginState

@rx.page(route="/login_screen",title="Login", image="/favicon.ico")
def login_screen() -> rx.Component:
    return rx.center(
        rx.card(
            rx.vstack(
                rx.center(
                    rx.image(
                        src="/logo_letras_negro.webp",
                        width="10em",
                        height="auto",
                        border_radius="25%",
                    ),
                    rx.heading(
                        "Mena Plaza Dashboard",
                        size="6",
                        as_="h2",
                        text_align="center",
                        width="100%",
                    ),
                    direction="column",
                    spacing="5",
                    width="100%",
                ),
                rx.vstack(
                    rx.text(
                        "Email address",
                        size="3",
                        weight="medium",
                        text_align="left",
                        width="100%",
                    ),
                    rx.input(
                        placeholder="email",
                        type="email",
                        size="3",
                        width="100%",
                        on_change=LoginState.set_email,
                    ),
                    justify="start",
                    spacing="2",
                    width="100%",
                ),
                rx.vstack(
                    rx.text(
                        "Password",
                        size="3",
                        weight="medium",
                    ),
                    rx.input(
                        placeholder="Introduce contraseña",
                        type="password",
                        size="3",
                        width="100%",
                        on_change=LoginState.set_password,
                    ),
                    spacing="2",
                    width="100%",
                ),
                rx.button(
                    "Entrar",
                    size="3",
                    width="100%",
                    on_click=LoginState.login,
                    bg="blue.500",
                    color="white",
                    _hover={"bg": "blue.100"},
                ),
                rx.text(
                    LoginState.error,
                    color="red",
                    visibility=rx.cond(LoginState.error, "visible", "hidden"),
                ),
                spacing="6",
                width="100%",
            ),
            size="4",
            max_width="28em",
            width="100%",
            padding="2em",
            box_shadow="lg",
            
        ),
        align="center",
        bg="#E7EEF7",
        height="100vh"
    )