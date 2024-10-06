import reflex as rx
from mena_reservation_form.state.form_template_state import ReservationTemplateState
from mena_reservation_form.state.translation_state import Translation_state

def reservation_form_template():
    return rx.form(
        rx.vstack(
            rx.heading("DATOS RESERVA", width="100%", align="center"),
            rx.input(placeholder="Nombre recepcionista", name="reception_name", required=True),
            rx.select(
                ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10"],
                name="rooms_to_reserve",
                required=True,
                placeholder="número de habitaciones",
            ),
            rx.input(
                placeholder="Check-in date ",
                name="check_in_date",
                type="date",
                on_change=lambda val: ReservationTemplateState.update_dates(val, True),
                required=True
            ),
            rx.input(
                placeholder="Check-out Date",
                name="check_out_date",
                type="date",
                on_change=lambda val: ReservationTemplateState.update_dates(val, False),
                required=True
            ),
            rx.checkbox("Precio Genius -10%", name="price_genius"),
            rx.checkbox("Precio Long Stay -5%", name="price_long_stay"),
            rx.input(placeholder="Precio (Aloj) 1", name="price_stay1", type="double", required=True),
            rx.input(placeholder="Precio (Aloj + Des) 1", name="price_accommodation_breakfast1"),
            rx.cond(
                ReservationTemplateState.show_additional_prices,
                rx.vstack(
                    rx.input(placeholder="Precio (Aloj) 2", name="price_stay2", type="double"),
                    rx.input(placeholder="Precio (Aloj + Des) 2", name="price_accommodation_breakfast2"),
                )
            ),
            rx.button("Completar Plantilla", type="submit"),
            rx.button(
                "Copiar y exportar",
                color_scheme="crimson",
                on_click=ReservationTemplateState.copy_template,
            ),
            align="left",
        ),
        on_submit=[ReservationTemplateState.handle_submit],
    )