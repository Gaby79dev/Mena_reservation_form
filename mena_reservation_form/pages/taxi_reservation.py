import reflex as rx
from mena_reservation_form.state.translation_state import Translation_state
from mena_reservation_form.state.taxi_form_state import TaxiFormState as State
from mena_reservation_form.components.footer import footer
from mena_reservation_form.components.navbar import navbar


@rx.page(title="Taxi Reservation Form", image="/favicon.ico")
def taxiReservation() -> rx.Component:
    return rx.vstack(
        navbar(),
        rx.card(
            rx.heading(
                Translation_state.reservation_form_translation_taxi_title, 
                width="100%", 
                align="center",
            ),
            rx.spacer(height="2em"),
            rx.form.root(
                rx.vstack(
                    rx.form.field(
                        rx.hstack(
                            rx.text(
                                f"* {Translation_state.reservation_form_tranlation_taxi_name}", 
                                weight="bold",
                                align_self="start",
                                width="50%",
                                auto_capitalize=True
                            ),
                            rx.spacer(width="1em"),
                            rx.input(
                                value=State.reservation_name,
                                on_change=State.set_reservation_name,
                                required=True,
                                align="left",
                                width="50%"
                            ),
                            align="center"
                        ),
                        name="reservation_name",
                        width="100%"                        
                    ),
                    rx.form.field(
                        rx.hstack(
                            rx.text(
                                f"* {Translation_state.reservation_form_translation_taxi_arrival_date}", 
                                weight="bold",
                                align_self="start",
                                width="50%"
                            ),
                            rx.spacer(width="1em"),
                            rx.input(
                                type="date",
                                value=State.reservation_date,
                                on_change=State.set_resevation_date,
                                required=True,
                                align="center",
                                text_align = "right",
                                align_self="center",
                                width="50%"
                            ),
                            align="center"
                        ),
                        name="reservation_date",
                        width="100%", 
                    ),
                    rx.form.field(
                        rx.hstack(   
                            rx.text(
                                f"* {Translation_state.reservation_form_translation_phone_number}",
                                weight="bold",
                                width="50%"
                            ),
                            rx.spacer(width="1em"),
                            rx.input(
                                value=State.phone_number,
                                on_change=State.set_phone_number,
                                required=True,
                                align="left",
                                width="50%"
                            ),
                        ),
                        name="phone_number",
                        width="100%"
                    ),
                    rx.form.field(
                        rx.hstack(   
                            rx.text(
                                f"* {Translation_state.reservation_form_translation_email_adress}",
                                weight="bold",
                                width="50%"
                            ),
                            rx.spacer(width="1em"),
                            rx.input(
                                type="email",
                                value=State.email_adress,
                                on_change=State.set_email_adress,
                                required=True,
                                align="left",
                                width="50%"
                            ),
                        ),
                        name="email_address",
                        width="100%"
                    ),
                    rx.form.field(
                        rx.hstack(
                            rx.text(
                                f"* {Translation_state.reservation_form_translation_passenger_number}", 
                                weight="bold",
                                width="50%"
                            ),
                            rx.spacer(width="1em"),
                            rx.input(                                
                                max_length=2,
                                value=State.passenger_number,
                                required= True,                                
                                on_change=State.set_passenger_number,
                                width="50%"
                            ),
                            align="center"
                        ),
                        name="passenger_number",
                        width="100%"
                    ),
                    rx.form.field(
                        rx.hstack(
                            rx.text(
                                f"* {Translation_state.reservation_form_translation_taxi_flight_number}", 
                                weight="bold",
                                width="50%"
                            ),
                            rx.spacer(width="1em"),
                            rx.input(
                                value=State.flight_number,
                                on_change=State.set_flight_number,
                                width="50%"
                            ),
                            align="center"
                        ),
                        name="flight_number",
                        width="100%"
                    ),
                    rx.form.field(
                        rx.hstack(
                            rx.text(
                                f"* {Translation_state.reservation_form_translation_taxi_arrival_time}", 
                                weight="bold",
                                width="50%"
                            ),
                            rx.spacer(width="1em"),
                            rx.input(
                                type="time",
                                value=State.time_arrival,
                                on_change=State.set_time_arrival,
                                width="50%" 
                            ),
                            align="center"
                        ),
                        name="time_arrival",
                        width="100%"
                    ),
                    rx.form.field(
                        rx.card(
                            rx.hstack(
                                rx.text(
                                    Translation_state.reservation_form_translation_taxi_price, 
                                    weight="bold",
                                    color_scheme="indigo"
                                ),
                                rx.text(
                                    f"{State.price}€",
                                    align="center",
                                    weight="bold",
                                    color_scheme="indigo",
                                ),
                                align="center",
                                justify="center"
                            ),
                            background="blue",
                            width="100%",
                            align = "center"
                        ),
                        name="price",
                        width="100%",
                        align ="center"
                    ),
                    rx.spacer(height="2em"),
                    rx.form.field(
                        rx.text(
                            Translation_state.reservation_form_translation_observation,
                            weight="bold"
                        ),
                        rx.spacer(),
                        rx.text_area(
                            value=State.observation,
                            on_change=State.set_observation,
                            width="100%",
                        ),
                        name="observation",
                        width="100%",
                    ),
                    rx.spacer(height="2em"),
                    rx.text(
                        Translation_state.reservation_form_translation_mandatory_field, 
                            align_self="start", 
                            size="2",
                            style={'font-style' : 'italic'}
                        ),
                    rx.form.submit(
                        rx.button(
                            Translation_state.reservation_form_translation_button_submit, 
                            align_self="center",
                            bg="#61728D",
                            width="100%",
                            disabled= rx.cond(
                                State.is_submit_enabled,
                                False,  # Si is_submit_enabled es verdadero, disabled será False (habilitado)
                                True    # Si is_submit_enabled es falso, disabled será True (deshabilitado)
                            ),
                        ),
                        as_child=True,
                    ),
                ),                
                on_submit=State.handle_send_taxi_email_and_message(),
                reset_on_submit=True
            ),
            rx.cond(
                State.email_sent_successfully,
                rx.hstack(
                    rx.image(src="/sobre_envio.png", height="30px"),
                    rx.image(src="/check_ic.png", height="30px"),
                    justify="center",  
                    width="100%",  
                ),
            ),
            
            bg="#EBF2FB",
            margin_top="60px"  
        ),
            footer(),         
        
        align="center",
        bg="#E7EEF7",
        
    )
