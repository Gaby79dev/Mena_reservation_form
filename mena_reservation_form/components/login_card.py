import reflex as rx

def login_card():
    return rx.center(
        rx.card(
            rx.vstack(
                rx.text(
                    "No estás logeado",
                    color="red.600",
                    font_size="1.5em",
                    font_weight="bold",
                    text_align="center",
                ),
                rx.icon(tag="lock_keyhole"),
                rx.link(
                    "Ir al login",
                    href="/",
                    color="blue.500",
                    text_decoration="none",
                    font_size="1.2em",
                    _hover={"color": "blue.700", "text_decoration": "underline"},
                    justify="center",
                ),
                spacing="1em",
                padding="2em",
                align="center"
            ),
            bg="#9bb6cd",
            box_shadow="0 4px 6px rgba(0, 0, 0, 0.1)",
            border_radius="lg",
            padding="3em",
            width="auto",
            max_width="400px",
        ),
        min_height="100vh",
        bg="gray.100",
        padding="2em",
    )