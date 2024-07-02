import reflex as rx
from ..state.translation_state import Translation_state

def footer() -> rx.Component:
        return rx.vstack(
            rx.vstack(   
                rx.box( 
                    rx.text(
                        Translation_state.reservation_form_responsible,
                        align_self="center",
                        size="1"                
                    ),
                    width="100%"
                ),
                rx.box( 
                    rx.text(
                        Translation_state.reservation_form_purpose,
                        align_self="center",
                        size="1"                
                    ),
                    width="100%"
                ),
                rx.box( 
                    rx.text(
                        Translation_state.reservation_form_legitimacy,
                        align_self="center",
                        size="1"                
                    ),
                    width="100%"
                ),
                rx.box( 
                    rx.text(
                        Translation_state.reservation_form_recipients,
                        align_self="center",
                        size="1",
                        style={}               
                    ),
                    width="100%"
                ),
                align="center",
                spacing="1"                
            ),          
            rx.spacer(spacing='9'),
            rx.hstack(
                rx.text(
                    "© Desarrollado por Gabriel Visiedo con ",
                    size="2",
                    color_scheme="plum",
                    weight="bold"
                ),
                rx.link(
                    rx.image(src="https://reflex.dev/logos/light/reflex.svg", width="60px"),
                    href="https://reflex.dev/",
                ),
                align="center",
                margin_bottom="20px"
            ),
            align="center",
            width="100%",
            height="100%",
            
        )
        
    