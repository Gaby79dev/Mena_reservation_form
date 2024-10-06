import reflex as rx
from mena_reservation_form.components.reservation_form_sidebar import reservation_form_template
from mena_reservation_form.state.form_template_state import ReservationTemplateState

def sidebar() -> rx.Component:
    return rx.box(
        rx.desktop_only(
            rx.vstack(
                rx.hstack(
                    rx.image(
                        src="/logo_hotel.png",
                        width="2.25em",
                        height="auto",
                        border_radius="25%",
                    ),
                    rx.text(
                        "Plantillas Reservas", size="6", weight="bold"
                    ),
                    align="center",
                    justify="start",
                    padding_x="0.5rem",
                    width="100%",
                ),
                sidebar_items(),
                rx.spacer(),
                reservation_form_template(),  # Agregar el formulario aquí
                spacing="5",
                padding_x="1em",
                padding_y="1.5em",
                bg="#b8ccdd",
                align="start",
                height="100vh",
                width="16em",
            ),
        ),
        rx.mobile_and_tablet(
            rx.drawer.root(
                rx.drawer.trigger(
                    rx.icon("align-justify", size=30)
                ),
                rx.drawer.overlay(z_index="5"),
                rx.drawer.portal(
                    rx.drawer.content(
                        rx.vstack(
                            rx.box(
                                rx.drawer.close(
                                    rx.icon("x", size=30)
                                ),
                                width="100%",
                            ),
                            sidebar_items(),
                            reservation_form_template(),  # Agregar el formulario aquí
                            spacing="5",
                            width="100%",
                        ),
                        top="auto",
                        right="auto",
                        height="100vh",
                        width="20em",
                        padding="1.5em",
                        bg="#9bb6cd",
                    ),
                    width="100%",
                ),
                direction="left",
            ),
            padding="1em",
        ),      
    )
def sidebar_item(text: str, image: str, template_name: str):
    return rx.box(
        rx.hstack(
            rx.image(src=image, width="30px", height="auto"),
            rx.text(text, size="4"),            
            width="100%",
            padding_x="0.5rem",
            padding_y="0.75rem",
            align="center",
            style={
                "_hover": {
                    "bg": rx.color("accent", 4),
                    "color": rx.color("accent", 11),
                },
                "border-radius": "0.5em",
            },
        ),
        on_click=lambda: ReservationTemplateState.set_template(template_name),
        cursor="pointer",
        width="100%",
    )

def spanish_flag_button(template_name: str):
    return rx.image(
        src="https://cdn-icons-png.flaticon.com/128/330/330557.png",
        width="30px",
        height="auto",
        cursor="pointer",
        on_click=lambda: ReservationTemplateState.set_template(f"{template_name}_es"),
    )

def sidebar_items():
    return rx.vstack(
        rx.hstack(
            sidebar_item("Double room", "/double_bed.png", "double_room"),
            spanish_flag_button("double_room"),
        align="center",
        width="100%"
        ),
        rx.hstack(
            sidebar_item("Family room", "/family_room.png", "family_room"),
            spanish_flag_button("family_room"),
        align="center",
        width="100%"
        ),
        rx.hstack(
            sidebar_item("Apartment", "/house.png", "apartment"),
            spanish_flag_button("apartment"),
            align="center",
        width="100%"
        ),
        rx.hstack(
            sidebar_item("Taxi", "/house.png", "taxi"),
            spanish_flag_button("taxi"),
            align="center"
        ),
        spacing="1",
        width="100%",
    )