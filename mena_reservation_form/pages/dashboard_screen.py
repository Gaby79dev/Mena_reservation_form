import reflex as rx
from mena_reservation_form.state.login_state import LoginState
from mena_reservation_form.state.navigation_state import NavigationState
from mena_reservation_form.components.login_card import login_card

@rx.page(route="/dashboard", title="Dashboard", image="/assets/favicon.ico")
def dashboard_screen() -> rx.Component:
    return rx.cond(
        LoginState.is_authenticated,
        rx.container(
            rx.vstack(
                rx.flex(
                    rx.heading("HOTEL MENA PLAZA DASHBOARD", 
                        size="8", 
                        margin_bottom="20px",
                        margin_top="10px",
                        color="#201E43"
                    ),
                    width="100%",
                    justify="center",
                ),
                rx.flex(
                    create_card("Plantillas emails Hotel", "Create, edit, and delete room templates.", "Go to Templates", NavigationState.navigate_to_room_templates),
                    create_card("Cumpleaños Mena", "View and manage current bookings.", "View Bookings", NavigationState.navigate_to_confirmation_screen),
                    
                    wrap="wrap",
                    justify="center",
                    spacing="4",
                ),
                width="100%",
                max_width="1200px",
                margin="auto",
                padding="50px",
            ),
            min_height="100vh",
            bg="#E7EEF7"
        ),
        rx.center(
            login_card(),
        min_height="100vh",
        bg="gray.100",
        padding="2em",
        )
    )

def create_card(title, description, button_text, navigate):
    return rx.card(
        rx.vstack(
            rx.heading(title, size="lg", color="#201E43"),
            rx.text(description, color="gray.600"),
            rx.spacer(),
            rx.button(
                button_text, 
                color_scheme="cyan", 
                size="md",
                margin_bottom="10px",
                on_click= navigate
            ),
            align="center",
            spacing="2",
            height="100%",
        ),
        box_shadow="lg",
        border_radius="lg",
        padding="30px",
        bg="#6fade2",
        width="350px",
        height="200px",
    )