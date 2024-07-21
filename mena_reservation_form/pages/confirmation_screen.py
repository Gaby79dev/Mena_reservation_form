import reflex as rx

# Definir estilos comunes reutilizables
common_text_style = {"text_align": "center", "font_size": "xl"}
common_card_style = {
    "padding": "20px",
    "text_align": "center",
    "border_radius": "10px",
    "box_shadow": "0 4px 8px rgba(0, 0, 0, 0.1)",
    "bg_color" : "#D2E4EC" 
}

# Función que crea la pantalla de confirmación
def confirmation_screen():
    card_content = rx.vstack(
        rx.hstack( 
            rx.image(
                src="https://firebasestorage.googleapis.com/v0/b/mena-garden-87c52.appspot.com/o/logo_y_letras_negro.png?alt=media&token=448f6e5c-9c59-403d-9bb9-150936177425",
                style={"margin_bottom": "20px"},
                width="100px",
                height="auto",   
            ),
            rx.image(
                src="/check_ic.png",
                alt="Check_in_logo",
                style={"margin_bottom": "20px"}
            ),
        ),
        rx.heading(
            "Su mensaje ha sido enviado.",
            font_size="4xl",
            font_weight="bold",
            color_scheme="green",
            style = common_text_style
        ),
        rx.text(
            "Tras la revisión de los datos por el personal del departamento de reservas, "
            "recibirá la confirmación lo antes posible.",
            style = common_text_style
        ),
        rx.divider(),
        rx.heading(
            "Your message has been sent.",
            font_size="4xl",
            font_weight="bold",
            color_scheme="green",
            style=common_text_style
        ),
        rx.text(
            "After the data review by the reservations department staff, you will receive the confirmation as soon as possible.",
            style=common_text_style
        ),
        rx.spacer(height="50px"),
        rx.hstack(
            rx.text(
                "Thank you - Gracias - Danke - Merci - Grazie",                    
                size="2",
                weight="bold",
                width="100%",
                align="center",            
            ),
            width = "100%",
            justify="center",
        ),
    )
    return rx.box(
        rx.center(
            rx.card(
                card_content,
                size="2",
                variant="ghost",
                style=common_card_style
            ),
            style={"height": "100vh"}
        ),
        style={"background_color": "#f0f0f0", "height": "100vh"}
    )
