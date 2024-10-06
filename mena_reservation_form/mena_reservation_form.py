import reflex as rx
from rxconfig import config
from .pages.reservation_form import reservationForm
from .pages.taxi_reservation import taxiReservation
from .pages.confirmation_screen import confirmation_screen
from .pages.login_screen import login_screen
from .pages.room_templates import room_templates
from .pages.dashboard_screen import dashboard_screen


@rx.page(title="Hotel Mena Plaza Login", image="/favicon.ico")
def index() -> rx.Component:
    return rx.box( 
        login_screen(),
        rx.hstack(
            rx.text(
                "© Desarrollado por Gabriel Visiedo con ",
                size="2",
                color_scheme="plum",
                weight="bold",
            ),
            rx.link(
                rx.image(src="https://reflex.dev/logos/light/reflex.svg"),
                href="https://reflex.dev/",
                width="80px",
                height="auto"
            ),
            justify_content="center",  # Center align the items within the hstack
            margin_bottom="20px",
            width="100%",
        ),
        width="100%",
        bg="#E7EEF7",       
    )


app = rx.App(
    theme=rx.theme(
        has_background=True,
        
    )
)

app.add_page(index, route=('/'))
app.add_page(dashboard_screen, route="/dashboard")
app.add_page(taxiReservation, route=('/taxi_reservation'))
app.add_page(confirmation_screen, route=('/confirmation_screen'))
app.add_page(login_screen, route=('/login_screen'))
app.add_page(room_templates, route=('/room_templates'))
app.add_page(reservationForm, route=('/hotel_reservation'))


app._compile()