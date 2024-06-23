
import reflex as rx
from rxconfig import config
from .components.navbar import navbar
from .pages.reservation_form import reservationForm
from .pages.taxi_reservation import taxiReservation
from .pages.confirmation_screen import confirmation_screen
from .components.footer import footer


@rx.page(title="Hotel Mena Reservation Form", image="/favicon.ico")
def index() -> rx.Component:
    return rx.flex(
        rx.vstack(
            navbar(),
            rx.spacer(spacing='4'),
            reservationForm(),
            footer(),
            
        width="100%",
        bg="#E7EEF7",
        align="center"
        )
    )

app = rx.App(
    theme=rx.theme(
        has_background=True,
        
    )
)

app.add_page(index, route=('/'))
app.add_page(taxiReservation, route=('/taxi_reservation'))
app.add_page(confirmation_screen, route=('/confirmation_screen'))

app._compile()