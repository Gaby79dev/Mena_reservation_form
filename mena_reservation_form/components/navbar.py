import reflex as rx
from mena_reservation_form.state.translation_state import Translation_state
from mena_reservation_form.state.navigation_state import NavigationState

def navbar() -> rx.Component:
    return rx.box(
        rx.flex(
            rx.image(
                src="/logo_letra_plateado.png",
                width="150px",
                height="auto",
            ),
            rx.flex(
                rx.image(
                    src="https://cdn-icons-png.flaticon.com/128/330/330557.png",
                    width="25px",
                    align="center",
                    style={'marging_right' :'30px'},
                    on_click=lambda: Translation_state.set_language('es'),
                    
                ),
                
                rx.image(
                    src="https://cdn-icons-png.flaticon.com/128/330/330425.png",
                    width="25px",
                    align="center",
                    on_click=lambda: Translation_state.set_language('en')
                ),
                rx.spacer(width="5"),
                taxi_form_button(), # Primer botón
                reservation_form_button(), # Segundo botón
                direction="row",
                align_items="center",
                justify_content="start",
                bg="#61728D",
                wrap="wrap",
                spacing="2"
            ),
            align_items="center",
            justify_content="start",
            width="100%",
            bg="#61728D",
            wrap="wrap"
        ),
        width="100%",
        padding="2em",
        bg="#61728D"
    )

def reservation_form_button() -> rx.Component:
    return rx.button(
        "Taxi Reservation",
        variant="surface",
        border_radius="lg",
        color_scheme="blue",
        on_click=lambda: NavigationState.navigate_to_taxi_form(),
        style={"margin": "5px"}
    )

def taxi_form_button() -> rx.Component:
    return rx.button(
        "Reservation Form",
        variant="surface",
        border_radius="lg",
        color_scheme="blue",
        on_click=lambda: NavigationState.navigate_to_hotel_form(),
        style={"margin": "5px"}
    )