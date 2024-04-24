from rxconfig import config
from .components.navbar import navbar
from .components.header import header

import reflex as rx

@rx.page(title="Hotel Mena reservation form", image="/favicon.ico")
def index() -> rx.Component:
    return rx.flex(
        rx.vstack(
            navbar(),
            rx.spacer(spacing='4'),
            header(),
            rx.spacer(spacing='9'),
            rx.hstack(
                rx.text(
                    "© Developed by VipeDev with ",
                    size="2",                
                ),
                rx.link(
                    rx.image(src="https://reflex.dev/logos/light/reflex.svg", 
                    width="60px"),
                    href="https://reflex.dev/",
                ),
                align="center",
                margin_bottom="12px"
            ),
            align="center",
            width="100%",
            height="100%",
            flex_grow=1,
        ),
        width="100%",
        height="100vh",  # Ajuste para ocupar toda la altura de la ventana.
        bg="#F2F4F7",
        flex_grow=1,  # Añadido para que el contenedor flex crezca y ocupe el espacio disponible.
    )

app = rx.App(
    theme=rx.theme(
        has_background=True,
        bg="#F2F4F7"
    )
)
app.add_page(index)
