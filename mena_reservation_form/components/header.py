import reflex as rx
from mena_reservation_form.state.form_state import ReservationFormState as State
from mena_reservation_form.state.translation_state import Translation_state

def header() -> rx.Component:
    return rx.vstack(
        rx.card(
            rx.heading(
                Translation_state.reservation_form_translation, 
                width="100%", 
                align="center",
            ),
            rx.spacer(height="2em"),
            rx.form.root(
                rx.vstack(
                    rx.form.field(
                        rx.hstack(
                            rx.text(
                                f"* {Translation_state.reservation_form_translation_name}", 
                                weight="bold",
                                align_self="start",
                                ),
                            rx.spacer(width="1em"),    
                            rx.input.input(
                                value=State.reservation_name,
                                on_change=State.set_reservation_name,
                                required=True,
                                align="left",
                                width="75%"
                            ),
                            align="center"                            
                        ),
                        name="reservation_name",
                        width="100%"                        
                    ),
                    rx.form.field(
                        rx.hstack(
                            rx.text(
                                f"* {Translation_state.reservation_form_translation_check_in}", 
                                weight="bold",
                                align_self="start", # Alinea el texto a la izquierda
                            ),
                            rx.spacer(width="1em"),
                            rx.input.input(
                                value=State.check_in,
                                on_change=State.set_check_in,
                                required=True,
                                align="left",
                                width="75%" # asegurarse de que el ancho sea consistente
                            ),
                            align="center"
                        ),
                        name="check_in",
                        width="100%" 
                    ),
                    rx.form.field(
                        rx.hstack(
                            rx.text(
                                f"* {Translation_state.reservation_form_translation_check_out}", 
                                weight="bold",
                                align_self="start", # Alinea el texto a la izquierda
                            ),
                            rx.spacer(width="1em"),
                            rx.input.input(
                                value=State.check_out,
                                on_change=State.set_check_out,
                                required=True,
                                align="left",
                                width="75%" 
                            ),
                        align="center"
                        ),
                        name="check_out",
                        width="100%" 
                    ),
                    rx.form.field(
                        rx.hstack(   
                            rx.text(
                                f"* {Translation_state.reservation_form_translation_phone_number}",
                                weight="bold"
                                ),
                            rx.spacer(width="1em"),
                            rx.input.input(
                                value=State.phone_number,
                                on_change=State.set_phone_number,
                                required=True,
                                align="left",
                                width="75%"
                            ),
                        ),
                        name="phone_number",
                        width="100%"
                    ),
                    rx.form.field(
                        rx.hstack(   
                            rx.text(
                                f"* {Translation_state.reservation_form_translation_email_adress}",
                                weight="bold"
                                ),
                            rx.spacer(width="1em"),
                            rx.input.input(
                                value=State.email_adress,
                                on_change=State.set_email_adress,
                                required=True,
                                align="left",
                                width="75%"
                            ),
                        ),
                        name="phone_number",
                        width="100%"
                    ),
                    rx.form.field(
                        rx.hstack(
                            rx.text(
                                f"* {Translation_state.reservation_form_translation_accommodation_type}", 
                                weight="bold"
                                ),
                            rx.spacer(width="1em"),
                            rx.select(
                                [Translation_state.reservation_form_translation_only_stay, Translation_state.reservation_form_translation_breakfast_stay],
                                on_change=State.set_accommodation_type,                            
                                required=True,
                                width="48.5%",
                            ),
                        align="center"
                        ),
                        name="accommodation_type",
                        width="100%"
                    ),
                    rx.form.field(
                        rx.hstack(
                            rx.image(src="/tc_lock.webp", height="30px"),
                            rx.checkbox(
                                text=Translation_state.reservation_form_tranlation_show_numbers,
                                on_change=State.toggle_show_numbers,
                            ),
                            name="show_credit_card_numbers",
                            align="center"
                        ),
                        width="100%", 
                    ),
                    rx.form.field(                      
                            rx.hstack(
                                rx.text(
                                    f"* {Translation_state.reservation_form_translation_card_number}",
                                    weight="bold"
                                ),
                                rx.spacer(width="1em"),
                                rx.input.input(
                                    value=State.credit_card_number,
                                    on_change=State.set_credit_card_number,
                                    required=True,
                                    align="left",
                                    width="75%",
                                    max_length="19",
                                    type= rx.cond(
                                        State.show_credit_card_numbers,
                                        "text",
                                        "password"
                                    ),
                                
                                ),   
                            align="center"                             
                            ),
                        name="card_number",
                        width="100%"
                    ),
                    rx.form.field(
                            rx.hstack( 
                                rx.text(
                                    f"* {Translation_state.reservation_form_translation_expirate_date}",
                                    weight="bold"
                                ),   
                                rx.spacer(width="1em"),
                                rx.input.input(
                                    value=State.expiration_date,
                                    on_change=State.set_expiration_date,
                                    required=True,
                                    placeholder="(MM/YY)",
                                ),
                                align="center"
                            ),
                        name="expiration_date",
                        width="100%",
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
                        name="Observations",
                        width="100%",
                    ),
                    rx.spacer(height="2em"),
                    rx.text("* campos obligatorios", align_self="center", size="2", color_scheme="red"),
                    rx.form.submit(
                        rx.button(
                            Translation_state.reservation_form_translation_button_submit, 
                            align_self="center",
                            bg ="#61728D",
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
                on_submit=State.handle_send_email_and_message,
                reset_on_submit=True,
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
            bg = "#EBF2FB"                
        ),
        margin_top="50px",
        align="center",
        bg="#E7EEF7"
    )