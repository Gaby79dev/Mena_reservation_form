import reflex as rx
from mena_reservation_form.state.translation_state import Translation_state


def navbar() -> rx.Component:
    return rx.flex(
        rx.box(
            rx.hstack(
                rx.image(
                    src="https://www.hotelmenaplaza.es/wp-content/uploads/2016/03/1412545810_1381312738_logo_hotel.png",
                    height="100%",
                    width="200px",
                    padding_top="8px",
                ),
                rx.image(
                    src="https://cdn-icons-png.flaticon.com/128/330/330557.png",
                    width="30px",
                    align="center",
                    on_click=lambda: Translation_state.set_language('es'),  # Cambia el idioma a español
                    
                ),
                rx.image(
                    src="https://cdn-icons-png.flaticon.com/128/330/330425.png",
                    width="30px",
                    align="center",
                    on_click=lambda: Translation_state.set_language('en'),  # Cambia el idioma a inglés
                ),
                spacing="4",
            ),
        ),
        rx.spacer(),  
        background_color="#000000",
        justify_content="center", 
        align_items="center", 
        width="100%",
        padding="1em",
        bg="#61728D"
    )