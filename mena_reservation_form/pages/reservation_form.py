import reflex as rx
from mena_reservation_form.state.form_state import ReservationFormState as State
from mena_reservation_form.state.translation_state import Translation_state


def reservationForm() -> rx.Component:
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
                    # Campos del formulario...
                    rx.form.field(
                        rx.hstack(
                            rx.text(
                                f"* {Translation_state.reservation_form_translation_name}", 
                                weight="bold",
                                align_self="start",
                                width="50%"
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
                                f"* {Translation_state.reservation_form_translation_check_in}", 
                                weight="bold",
                                align_self="start",
                                width="50%"
                            ),
                            rx.spacer(width="1em"),
                            rx.input(
                                type="date",
                                value=State.check_in,
                                on_change=State.set_check_in,
                                required=True,
                                align="left",
                                width="50%" # asegurarse de que el ancho sea consistente
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
                                align_self="start", 
                                width="50%"
                            ),
                            rx.spacer(width="1em"),
                            rx.input(
                                type="date",
                                value=State.check_out,
                                on_change=State.set_check_out,
                                required=True,
                                align="left",
                                width="50%" 
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
                                weight="bold",
                                width="50%"
                                ),
                            rx.spacer(width="1em"),
                            rx.input(
                                type="number",
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
                        name="phone_number",
                        width="100%"
                    ),
                    rx.form.field(
                        rx.hstack(
                            rx.text(
                                f"* {Translation_state.reservation_form_translation_accommodation_type}", 
                                weight="bold",
                                width="50%"
                                ),
                            rx.spacer(width="1em"),
                            rx.select(
                                [Translation_state.reservation_form_translation_only_stay, Translation_state.reservation_form_translation_breakfast_stay],
                                on_change=State.set_accommodation_type,                            
                                required=True,
                                width="50%",
                            ),
                        align="center"
                        ),
                        name="accommodation_type",
                        width="100%"
                    ),
                        rx.form.field(
                            rx.hstack(
                                rx.text(
                                    f"* {Translation_state.reservation_form_translation_rooms_to_reserve}", 
                                    weight="bold",
                                    width="50%"
                                    ),
                                rx.spacer(width="1em"),
                                rx.select(
                                    [
                                        Translation_state.reservation_form_translation_rooms_to_reserve_one, 
                                        Translation_state.reservation_form_translation_rooms_to_reserve_two,
                                        Translation_state.reservation_form_translation_rooms_to_reserve_three,
                                        Translation_state.reservation_form_translation_rooms_to_reserve_four,
                                        Translation_state.reservation_form_translation_rooms_to_reserve_five,
                                        Translation_state.reservation_form_translation_rooms_to_reserve_six,
                                        Translation_state.reservation_form_translation_rooms_to_reserve_seven,
                                        Translation_state.reservation_form_translation_rooms_to_reserve_eight,
                                        Translation_state.reservation_form_translation_rooms_to_reserve_nine,
                                        Translation_state.reservation_form_translation_rooms_to_reserve_ten,
                                    ],
                                    on_change=State.set_rooms_to_reserve,                            
                                    required=True,
                                    width="50%",
                                ),
                            align="center"
                            ),
                            name="accommodation_type",
                            width="100%"
                        ),
                    rx.form.field(
                        rx.vstack(
                            rx.text( 
                                f"* {Translation_state.reservation_form_translation_room_type}", 
                                weight="bold",
                                align="left",
                                width = "100%"
                                
                                ),
                            rx.select(
                                [
                                    Translation_state.reservation_form_translation_standar_room, 
                                    Translation_state.reservation_form_translation_superior_room,
                                    Translation_state.reservation_form_translation_superior_room_square,
                                    Translation_state.reservation_form_translation_family_room,
                                    Translation_state.reservation_form_translation_apartment
                                ],
                                on_change=State.set_superior_type,                            
                                required=True,
                                width="100%",
                            ),
                        align="center"
                        ),
                        name="stay_options",
                        width="100%"
                    ),
                    rx.form.field(
                        rx.hstack(
                            rx.image(src="/tc_lock.webp", height="30px"),
                            rx.checkbox(
                                text=Translation_state.reservation_form_tranlation_show_numbers,
                                on_change=State.toggle_show_numbers,
                                
                            ),
                            justify="end",
                            name="show_credit_card_numbers",
                            align="end"
                        ),
                        width="100%",
                    ),
                    rx.form.field(                      
                            rx.hstack(
                                rx.text(
                                    f"* {Translation_state.reservation_form_translation_card_number}",
                                    weight="bold",
                                    width="50%"
                                ),
                                rx.spacer(width="1em"),
                                rx.input(
                                    value=State.credit_card_number,
                                    on_change=State.set_credit_card_number,
                                    required=True,
                                    align="left",
                                    width="50%",
                                    max_length=16,
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
                                rx.input(
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
                            
        ),
        margin_top="50px",
        align="center",
)

