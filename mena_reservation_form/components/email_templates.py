
class EmailTemplates:

        # html para crear el formulario de la reserva recibido en email.
        @staticmethod
        def get_email_confirmation_reservation_template(
                image_url, 
                reservation_name,
                check_in_date,
                check_out_date,
                phone_number,
                email_adress,
                rooms_to_reserve,
                accommodation_type,
                superior_type,
                formatted_credit_card_number,
                expiration_date,
                observation,
                mailto_link_double_en,
                mailto_link_double_es,
                mailto_link_family_en,
                mailto_link_family_es,
                mailto_link_apartment_en,
                mailto_link_apartment_es
        ):
                return f"""
                        <html>
                        <head>
                        <style>
                                body {{
                                font-family: Arial, sans-serif;
                                margin: 0;
                                padding: 0;
                                background-color: white;
                                }}
                                .container {{
                                width: 100%;
                                padding: 20px;
                                display: flex;
                                justify-content: center;
                                }}
                                .content {{
                                width: 80%;
                                max-width: 600px;
                                background-color: #F3F3F3;
                                padding: 20px;
                                border-radius: 10px;
                                box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
                                }}
                                .header {{
                                background-color: #CBD3D8;
                                color: #4B5052;
                                padding: 10px;
                                text-align: center;
                                border-radius: 10px 10px 0 0;
                                }}
                                .header img {{
                                width: 150px; /* Ajusta el tamaño aquí */
                                height: auto;
                                display: block;
                                margin: 0 auto;
                                }}
                                .content table {{
                                width: 100%;
                                border-collapse: collapse;
                                }}
                                .content th, .content td {{
                                padding: 10px;
                                text-align: left;
                                border-bottom: 1px solid #ddd;
                                }}
                                .footer {{
                                text-align: center;
                                font-size: 12px;
                                color: #777;
                                margin-top: 20px;
                                }}
                                .button {{
                                border: none;
                                padding: 10px 20px;
                                text-align: center;
                                text-decoration: none;
                                display: inline-block;
                                font-size: 14px;
                                margin: 15px 2px;
                                cursor: pointer;
                                border-radius: 10px;
                                width: auto;
                                height: auto; /* Ajusta la altura del botón */
                                line-height:normal; /* Ajusta el centrado vertical del texto */
                                position: relative; /* Ajusta la posición de la imagen */
                                }}
                                .button.en {{
                                background-color: #4366A4; /* azul para inglés */
                                color: white;
                                }}
                                .button.es {{
                                background-color: #FF5733; /* Rojo para español */
                                color: white;
                                }}
                                .button img {{
                                height: 15px; /* Ajusta la altura deseada */
                                width: auto; /* Ajusta el ancho automático para mantener la proporción */
                                margin-right: 10px; /* Espacio entre la imagen y el texto */
                                vertical-align: middle; /* Alinea la imagen verticalmente con el texto */
                        }}
                        </style>
                        </head>
                        <body>
                        <div class="container">
                                <div class="content">
                                <div class="header">
                                        <img src="{image_url}" alt="Logo" />
                                        <h1>Reserva: {reservation_name}</h1>
                                </div>
                                <table>
                                        <tr>
                                        <td><strong>Fecha de entrada:</strong></td>
                                        <td>{check_in_date}</td>
                                        </tr>
                                        <tr>
                                        <td><strong>Fecha de salida:</strong></td>
                                        <td>{check_out_date}</td>
                                        </tr>
                                        <tr>
                                        <td><strong>Nº Teléfono:</strong></td>
                                        <td>{phone_number}</td>
                                        </tr>
                                        <tr>
                                        <td><strong>Email:</strong></td>
                                        <td>{email_adress}</td>
                                        </tr>
                                        <tr>
                                        <td><strong>Nº de rooms:</strong></td>
                                        <td>{rooms_to_reserve}</td>
                                        </tr>
                                        <tr>
                                        <td><strong>Tipo de Alojamiento:</strong></td>
                                        <td>{accommodation_type}</td>
                                        </tr>
                                        <tr>
                                        <td><strong>En régimen de:</strong></td>
                                        <td>{superior_type}</td>
                                        </tr>
                                        <tr>
                                        <td><strong>Número de tarjeta de crédito:</strong></td>
                                        <td>{formatted_credit_card_number}</td>
                                        </tr>
                                        <tr>
                                        <td><strong>Fecha de expiración:</strong></td>
                                        <td>{expiration_date}</td>
                                        </tr>
                                        <tr>
                                        <td><strong>Observaciones:</strong></td>
                                        <td>{observation}</td>
                                        </tr>
                                </table>
                                <div class="footer">
                                        <p>RESERVA DE FORMULARIO WEB</p>
                                        <div style="text-align: center;">
                                        <a href="{mailto_link_double_en}" class="button en">
                                                <img src="https://cdn-icons-png.flaticon.com/128/330/330425.png" alt="Imagen Inglés" /> Confirmar DOBLE inglés
                                        </a>
                                        <a href="{mailto_link_double_es}" class="button es">
                                                <img src="https://cdn-icons-png.flaticon.com/128/330/330557.png" alt="Imagen Español" /> Confirmar DOBLE español
                                        </a>
                                        <a href="{mailto_link_family_en}" class="button en">
                                                <img src="https://cdn-icons-png.flaticon.com/128/330/330425.png" alt="Imagen Español" /> Confirmar FAMILIAR inglés
                                        </a>
                                        <a href="{mailto_link_family_es}" class="button es">
                                                <img src="https://cdn-icons-png.flaticon.com/128/330/330557.png" alt="Imagen Español" /> Confirmar FAMILIAR español
                                        </a>
                                        <a href="{mailto_link_apartment_en}" class="button en">
                                                <img src="https://cdn-icons-png.flaticon.com/128/330/330425.png" alt="Imagen Español" /> Confirmar APARTAMENTO inglés
                                        </a>
                                        <a href="{mailto_link_apartment_es}" class="button es">
                                                <img src="https://cdn-icons-png.flaticon.com/128/330/330557.png" alt="Imagen Español" /> Confirmar APARTAMENTO español
                                        </a>
                                        </div>
                                </div>
                                </div>
                        </div>
                        </body>
                        </html>
                        """
        
        # html para crear el formulario del taxi recibido en email.
        @staticmethod
        def get_email_confirmation_taxi_template(
                image_url, 
                reservation_name,
                reservation_date_formatted,
                phone_number,
                email_adress,
                passenger_number,
                flight_number,
                time_arrival,
                price,
                observation,
                mailto_link_taxi_en,
                mailto_link_taxi_es                
        ):         
                return f"""
                <html>
                <head>
                <style>
                        body {{
                        font-family: Arial, sans-serif;
                        margin: 0;
                        padding: 0;
                        background-color: white;
                        }}
                        .container {{
                        width: 100%;
                        padding: 20px;
                        display: flex;
                        justify-content: center;
                        }}
                        .content {{
                        width: 80%;
                        max-width: 600px;
                        background-color: #E4EEF1;
                        padding: 20px;
                        border-radius: 10px;
                        box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
                        }}
                        .header {{
                        background-color: #E9E192;
                        color: #4B5052;
                        padding: 10px;
                        text-align: center;
                        border-radius: 10px 10px 0 0;
                        }}
                        .header img {{
                        width: 150px; /* Ajusta el tamaño aquí */
                        height: auto;
                        display: block;
                        margin: 0 auto;
                        }}
                        .content table {{
                        width: 100%;
                        border-collapse: collapse;
                        }}
                        .content th, .content td {{
                        padding: 10px;
                        text-align: left;
                        border-bottom: 1px solid #ddd;
                        }}
                        .footer {{
                        text-align: center;
                        font-size: 12px;
                        color: #777;
                        margin-top: 20px;
                        }}
                        .button {{
                        border: none;
                        padding: 10px 20px;
                        text-align: center;
                        text-decoration: none;
                        display: inline-block;
                        font-size: 14px;
                        margin: 15px 2px;
                        cursor: pointer;
                        border-radius: 10px;
                        width: auto;
                        height: auto; /* Ajusta la altura del botón */
                        line-height:normal; /* Ajusta el centrado vertical del texto */
                        position: relative; /* Ajusta la posición de la imagen */
                        }}
                        .button.en {{
                        background-color: #4366A4; /* azul para inglés */
                        color: white;
                        }}
                        .button.es {{
                        background-color: #FF5733; /* Rojo para español */
                        color: white;
                        }}
                        .button img {{
                        height: 15px; /* Ajusta la altura deseada */
                        width: auto; /* Ajusta el ancho automático para mantener la proporción */
                        margin-right: 10px; /* Espacio entre la imagen y el texto */
                        vertical-align: middle; /* Alinea la imagen verticalmente con el texto */
                        }}
                </style>
                </head>
                <body>
                <div class="container">
                        <div class="content">
                        <div class="header">
                                <img src="{image_url}" alt="Logo" />
                                <h1>Reserva Taxi: {reservation_name}</h1>
                        </div>
                        <table>
                                <tr>
                                <td><strong>Fecha de reserva:</strong></td>
                                <td>{reservation_date_formatted}</td>
                                </tr>
                                <tr>
                                <td><strong>Número de teléfono:</strong></td>
                                <td>{phone_number}</td>
                                </tr>
                                <tr>
                                <td><strong>Email:</strong></td>
                                <td>{email_adress}</td>
                                </tr>
                                <tr>
                                <td><strong>Número de pasajeros:</strong></td>
                                <td>{passenger_number}</td>
                                </tr>
                                <tr>
                                <td><strong>Número de vuelo:</strong></td>
                                <td>{flight_number}</td>
                                </tr>
                                <tr>
                                <td><strong>Hora de llegada:</strong></td>
                                <td>{time_arrival}</td>
                                </tr>
                                <tr>
                                <td><strong>Precio:</strong></td>
                                <td>{price}</td>
                                </tr>
                                <tr>
                                <td><strong>Observaciones:</strong></td>
                                <td>{observation}</td>
                                </tr>
                        </table>
                        <div class="footer">
                                <p>RESERVA DE FORMULARIO WEB TAXI</p>
                                <div style="text-align: center;">
                                <a href="{mailto_link_taxi_en}" class="button en">
                                        <img src="https://cdn-icons-png.flaticon.com/128/330/330425.png" alt="Imagen Inglés" /> Confirmar TAXI inglés
                                </a>
                                <a href="{mailto_link_taxi_es}" class="button es">
                                        <img src="https://cdn-icons-png.flaticon.com/128/330/330557.png" alt="Imagen Español" /> Confirmar TAXI español
                                </a>
                                </div> 
                        </div>
                        </div>
                </div>
                </body>
                </html>
                """

        @staticmethod
        def get_email_template_double_en(reservation_name, check_in_date, check_out_date, accommodation_type, superior_type,rooms_to_reserve, month_en):
                room_word_en = "room" if rooms_to_reserve == "one" else "rooms"
                room_prefix = "a" if rooms_to_reserve == "one" else rooms_to_reserve
                return f"""Dear {reservation_name},

        Thank you very much for trusting us and choosing Mena Plaza Hotel as your accommodation for an enjoyable stay in Nerja.

        I confirm the reservation of {room_prefix} double {room_word_en} for the following dates:
        
        Check-in: {check_in_date}
        Check-out: {check_out_date}

        The price for a double room during the month of {month_en} is _______ € per night ({accommodation_type}).
        
        We confirm a {superior_type}
        
        Please note that cancellations are free of charge if made 48 hours prior to arrival. In the event of cancellation outside this period or in case of no-show, 
        we will charge the first night of your stay on the provided credit card. 
        We also would like to inform you that any modifications or cancellations to your reservation will only be approved and confirmed via email to this same email address.
        
        If you have any questions, please do not hesitate to contact us.
        
        We look forward to welcoming you soon.
        
        Best regards,
        _________

        Reservation Department
        """

        @staticmethod
        def get_email_template_double_es(reservation_name, check_in_date, check_out_date, accommodation_type, superior_type,roooms_to_reserve, month_es):
                room_word_es = "habitación" if roooms_to_reserve == "una" else "habitaciones"
                double_room_word = "doble" if roooms_to_reserve == "una" else "dobles"
                return f"""Estimado/a {reservation_name},

        Muchas gracias por confiar en nosotros y elegir el Hotel Mena Plaza como su alojamiento para una estancia agradable en Nerja.

        Confirmo la reserva de {roooms_to_reserve} {room_word_es} {double_room_word} para las siguientes fechas:
        
        Fecha de entrada: {check_in_date}
        Fecha de salida: {check_out_date}
        
        El precio de la habitación doble durante el mes de {month_es} es de _______ € por noche ({accommodation_type}).
        
        Confirmamos un(a) {superior_type}.
        
        Tenga en cuenta que las cancelaciones son gratuitas si se realizan 48 horas antes de la llegada. En caso de cancelación fuera de este período o en caso de no presentarse,
        cargaremos la primera noche de su estancia en la tarjeta de crédito proporcionada. 
        También nos gustaría informarle que cualquier modificación o cancelación de su reserva solo será aprobada y confirmada a través de un correo electrónico a esta misma dirección.
        
        Si tiene alguna pregunta, no dude en ponerse en contacto con nosotros.
        
        Esperamos darle la bienvenida pronto.
        
        Atentamente,

        _________

        Departamento de Reservas
        """

        @staticmethod
        def get_email_template_family_en(reservation_name, check_in_date, check_out_date, accommodation_type, month_en, rooms_to_reserve):
                return f"""Dear {reservation_name},

        Thank you very much for trusting us and choosing Mena Plaza Hotel as your accommodation for an enjoyable stay in Nerja.

        I confirm the reservation of a family room for the following dates:
        
        Check-in: {check_in_date}
        Check-out: {check_out_date}

        The price for a family room  in the month of {month_en} is _______ € per night ({accommodation_type}).
        
        Please note that cancellations are free of charge if made 48 hours prior to arrival. In the event of cancellation outside this period or in case of no-show, 
        we will charge the first night of your stay on the provided credit card. 
        We also would like to inform you that any modifications or cancellations to your reservation will only be approved and confirmed via email to this same email address.
        
        If you have any questions, please do not hesitate to contact us.
        
        We look forward to welcoming you soon.
        
        Best regards,
        _________

        Reservation Department
        """

        @staticmethod
        def get_email_template_family_es(reservation_name, check_in_date, check_out_date, accommodation_type, month_es, rooms_to_reserve):
                return f"""Estimado/a {reservation_name},

        Muchas gracias por confiar en nosotros y elegir el Hotel Mena Plaza como su alojamiento para una estancia agradable en Nerja.

        Confirmo la reserva de una habitación familiar para cuatro personas para las siguientes fechas:
        
        Fecha de entrada: {check_in_date}
        Fecha de salida: {check_out_date}
        
        El precio de la habitación familiar durante el mes de {month_es} es de _______ € por noche ({accommodation_type}).
        
        Tenga en cuenta que las cancelaciones son gratuitas si se realizan 48 horas antes de la llegada. En caso de cancelación fuera de este período o en caso de no presentarse,
        cargaremos la primera noche de su estancia en la tarjeta de crédito proporcionada. 
        También nos gustaría informarle que cualquier modificación o cancelación de su reserva solo será aprobada y confirmada a través de un correo electrónico a esta misma dirección.
        
        Si tiene alguna pregunta, no dude en ponerse en contacto con nosotros.
        
        Esperamos darle la bienvenida pronto.
        
        Atentamente,

        _________

        Departamento de Reservas
        """

        @staticmethod
        def get_email_template_apartment_en(reservation_name, check_in_date, check_out_date, accommodation_type, month_en):
                return f"""Dear {reservation_name},

        Thank you very much for trusting us and choosing Mena Plaza Hotel as your accommodation for an enjoyable stay in Nerja.

        I confirm the reservation of a double bedroom apartment for the following dates:
        
        Check-in: {check_in_date}
        Check-out: {check_out_date}

        The price for the apartment during the month of {month_en} is _______ € per night ({accommodation_type}).

        The apartment does not include daily cleaning.
        
        Please note that cancellations are free of charge if made 48 hours prior to arrival. In the event of cancellation outside this period or in case of no-show, 
        we will charge the first night of your stay on the provided credit card. 
        We also would like to inform you that any modifications or cancellations to your reservation will only be approved and confirmed via email to this same email address.
        
        If you have any questions, please do not hesitate to contact us.
        
        We look forward to welcoming you soon.
        
        Best regards,
        _________

        Reservation Department
        """

        @staticmethod
        def get_email_template_apartment_es(reservation_name, check_in_date, check_out_date, accommodation_type, month_es):
                return f"""Estimado/a {reservation_name},

        Muchas gracias por confiar en nosotros y elegir el Hotel Mena Plaza como su alojamiento para una estancia agradable en Nerja.

        Confirmo la reserva de un apartamento de dos dormitorios para las siguientes fechas:
        
        Fecha de entrada: {check_in_date}
        Fecha de salida: {check_out_date}
        
        El precio de apartamento durante el mes de {month_es} es de _______ € por noche ({accommodation_type}).
        
        El apartamento no incluye limpieza diaria.

        Tenga en cuenta que las cancelaciones son gratuitas si se realizan 48 horas antes de la llegada. En caso de cancelación fuera de este período o en caso de no presentarse,
        cargaremos la primera noche de su estancia en la tarjeta de crédito proporcionada. 
        También nos gustaría informarle que cualquier modificación o cancelación de su reserva solo será aprobada y confirmada a través de un correo electrónico a esta misma dirección.
        
        Si tiene alguna pregunta, no dude en ponerse en contacto con nosotros.
        
        Esperamos darle la bienvenida pronto.
        
        Atentamente,

        _________

        Departamento de Reservas
        """

        @staticmethod
        def get_taxi_confirmation_en(reservation_date,time_arrival,reservation_name,price):
                return f""" Dear {reservation_name},

        Thank you for providing the information.

        I would like to confirm your taxi reservation for {reservation_date} at {time_arrival}.
        A taxi driver will be waiting for you at the airport arrivals, holding a sign with your name.
        The fare for the trip is {price}€ and can be paid directly to the driver, either by cash or card.

        Best regards,
        
        _________

        Reservation Department
        """

        @staticmethod
        def get_taxi_confirmation_es(reservation_date,time_arrival,reservation_name,price):
                return f"""Estimado/a {reservation_name},

        Gracias por proporcionar la información.

        Me gustaría confirmar su reserva de taxi para el día {reservation_date} a las {time_arrival}.
        Un taxista lo estará esperando en las llegadas del aeropuerto, sosteniendo un cartel con su nombre.
        La tarifa del viaje es de {price}€ y se puede pagar directamente al conductor, ya sea en efectivo o con tarjeta.

        Saludos cordiales,

        Departamento de Reservas
        """
