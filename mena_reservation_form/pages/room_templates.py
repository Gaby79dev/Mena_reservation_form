import reflex as rx
from mena_reservation_form.components.sidebar import sidebar
from mena_reservation_form.state.form_template_state import ReservationTemplateState
from mena_reservation_form.state.login_state import LoginState  
from mena_reservation_form.components.login_card import login_card

@rx.page(route="/room_templates", title="Plantillas Habitaciones", image="/favicon.ico")
def room_templates() -> rx.Component:
    return rx.cond(
        LoginState.is_authenticated,
        rx.hstack(
            sidebar(),
            rx.center(
                rx.box(
                    rx.heading(ReservationTemplateState.header_text),
                    rx.text(
                        ReservationTemplateState.email_preview, 
                        white_space="pre-wrap"
                    ),
                    padding="2em",
                    width="100%"
                ),
                width="100%"
            ),
            width="100%",
            bg="#f0f0f0"
        ),
        rx.center(
            login_card(),
        min_height="100vh",
        bg="gray.100",
        padding="2em",
        )
    )