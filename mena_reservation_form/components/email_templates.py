from datetime import datetime
from .utils import month_dict


class EmailTemplates:

        # html para crear el formulario de la reserva recibido en email.
        @staticmethod
        def get_email_confirmation_reservation_template(
                image_url, 
                reservation_name,
                check_in_date,
                check_out_date,
                phone_number,
                email_address,
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
                                        <td>{email_address}</td>
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
                email_address,
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
                                <td>{email_address}</td>
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
        def get_email_template_double_en(check_in_date, check_out_date, accommodation_type, superior_type,rooms_to_reserve, month_en):
                room_word_en = "room" if rooms_to_reserve == "one" else "rooms"
                room_prefix = "a" if rooms_to_reserve == "one" else rooms_to_reserve
                return f"""Dear guest,

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
        def get_email_template_double_es(check_in_date, check_out_date, accommodation_type, superior_type,roooms_to_reserve, month_es):
                room_word_es = "habitación" if roooms_to_reserve == "una" else "habitaciones"
                double_room_word = "doble" if roooms_to_reserve == "una" else "dobles"
                return f"""Estimado cliente,

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
        def get_email_template_family_en(check_in_date, check_out_date, accommodation_type, month_en, rooms_to_reserve):
                return f"""Dear guest,

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
        def get_email_template_family_es(check_in_date, check_out_date, accommodation_type, month_es, rooms_to_reserve):
                return f"""Estimado cliente,

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
        def get_email_template_apartment_en(check_in_date, check_out_date, accommodation_type, month_en):
                return f"""Dear guest,

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
        def get_email_template_apartment_es(check_in_date, check_out_date, accommodation_type, month_es):
                return f"""Estimado cliente,

        Muchas gracias por confiar en nosotros y elegir el Hotel Mena Plaza como su alojamiento para una estancia agradable en Nerja.

        Confirmamos la reserva de un apartamento de dos dormitorios para las siguientes fechas:
        
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
        def get_generate_print_template(
                reservation_name,
                image_url, 
                check_in_date,
                check_out_date,
                phone_number,
                email_address,
                rooms_to_reserve,
                accommodation_type,
                superior_type,
                formatted_credit_card_number,
                expiration_date,
                observation,
        ):
                return f"""
                <html>
                <head>
                <style>
                        body {{
                        font-family: Arial, sans-serif;
                        margin: 20px;
                        background-color: white;
                        color: black;
                        }}
                        .header {{
                        text-align: left;
                        margin-bottom: 20px;
                        }}
                        .header img {{
                        width: 250px; /* Ajusta el tamaño aquí */
                        height: auto;
                        display: inline-block; /* Cambiado de block a inline-block */
                        vertical-align: top; /* Alinea la imagen con el texto superior */
                        }}
                        .header h1 {{
                        margin: 10px 0 0 0;
                        display: inline-block; /* Hace que el título esté en línea con la imagen */
                        vertical-align: top; /* Alinea el texto con la parte superior de la imagen */
                        }}
                        .section {{
                        margin-top: 20px;
                        }}
                        .section h2 {{
                        margin-top: 0;
                        color: #4B5052;
                        background-color: #CBD3D8;
                        padding: 10px;
                        }}
                        .section p {{
                        margin: 10px 0;
                        }}
                        .footer {{
                        text-align: center;
                        font-size: 12px;
                        color: #777;
                        margin-top: 20px;
                        }}
                        .price-input {{
                        width: 100%;
                        padding: 10px;
                        margin-top: 10px;
                        border: 1px solid #ccc;
                        border-radius: 5px;
                        box-sizing: border-box;
                        }}
                </style>
                </head>
                <body>
                <div class="header">
                        <img src="{image_url}" alt="Logo" />
                        <h1>Reserva: {reservation_name}</h1>
                </div>

                <div class="section">
                        <h2>Detalles de la Reserva</h2>
                        <p><strong>Fecha de entrada:</strong> {check_in_date}</p>
                        <p><strong>Fecha de salida:</strong> {check_out_date}</p>
                        <p><strong>Nº Teléfono:</strong> {phone_number}</p>
                        <p><strong>Email:</strong> {email_address}</p>
                        <p><strong>Nº de habitaciones:</strong> {rooms_to_reserve}</p>
                        <p><strong>Tipo de Alojamiento:</strong> {accommodation_type}</p>
                        <p><strong>En régimen de:</strong> {superior_type}</p>
                        <p><strong>Número de tarjeta de crédito:</strong> {formatted_credit_card_number}</p>
                        <p><strong>Fecha de expiración:</strong> {expiration_date}</p>
                        <p><strong>Observaciones:</strong> {observation}</p>
                        <p><strong>Precio:</strong> <input type="text" class="price-input" placeholder="" /></p>
                </div>

                <div class="footer">
                        <p>RESERVA DE FORMULARIO WEB</p>
                        <p>&copy; 2024 Angesgar SL Todos los derechos reservados.</p>
                </div>
                </body>
                </html>
                """
        
        @staticmethod
        def _generate_double_price_en(form_data: dict):
                check_in = form_data.get("check_in_date", "")
                check_out = form_data.get("check_out_date", "")
                
                if check_in and check_out:
                        check_in_date = datetime.strptime(check_in, "%Y-%m-%d")
                        check_out_date = datetime.strptime(check_out, "%Y-%m-%d")
                        check_in_month = check_in_date.strftime("%B")
                        check_out_month = check_out_date.strftime("%B")
                else:
                        check_in_month = ""
                        check_out_month = ""
                
                price_info = f"The price for a double room in the month of {check_in_month} is {form_data.get('price_stay1', '')} € per night (Only Stay) and {form_data.get('price_accommodation_breakfast1', '')} € per night (Accommodation and Breakfast)"
                
                if check_in_month != check_out_month and check_out_date.day == 2:
                        price_info += f"\n\nThe price for a double room in the month of {check_out_month} is {form_data.get('price_stay2', '')} € per night (Only Stay) and {form_data.get('price_accommodation_breakfast2', '')} € per night (Accommodation and Breakfast)"
                
                return price_info
        
        @staticmethod
        def _generate_double_price_es(form_data: dict):
                check_in = form_data.get("check_in_date", "")
                check_out = form_data.get("check_out_date", "")
                
                if check_in and check_out:
                        check_in_date = datetime.strptime(check_in, "%Y-%m-%d")
                        check_out_date = datetime.strptime(check_out, "%Y-%m-%d")
                        check_in_month_en = check_in_date.strftime("%B")
                        check_out_month_en = check_out_date.strftime("%B")
                        check_in_month = month_dict.MONTHS_ES.get(check_in_month_en, check_in_month_en)
                        check_out_month = month_dict.MONTHS_ES.get(check_out_month_en, check_out_month_en)
                else:
                        check_in_month = ""
                        check_out_month = ""
                
                price_info = f"El precio de una habitación doble en el mes de {check_in_month} es de {form_data.get('price_stay1', '')} € por noche (Solo Estancia) y {form_data.get('price_accommodation_breakfast1', '')} € por noche (Alojamiento y Desayuno)"
                
                if check_in_month != check_out_month and check_out_date.day == 2:
                        price_info += f"\n\nEl precio de una habitación doble en el mes de {check_out_month} es de {form_data.get('price_stay2', '')} € por noche (Solo Estancia) y {form_data.get('price_accommodation_breakfast2', '')} € por noche (Alojamiento y Desayuno)"
                
                return price_info

        @staticmethod
        def _generate_family_price_en(form_data: dict):
                check_in = form_data.get("check_in_date", "")
                check_out = form_data.get("check_out_date", "")
                
                if check_in and check_out:
                        check_in_date = datetime.strptime(check_in, "%Y-%m-%d")
                        check_out_date = datetime.strptime(check_out, "%Y-%m-%d")
                        check_in_month = check_in_date.strftime("%B")
                        check_out_month = check_out_date.strftime("%B")
                else:
                        check_in_month = ""
                        check_out_month = ""
                
                price_info = f"The price for a family room in the month of {check_in_month} is {form_data.get('price_stay1', '')} € per night (Only Stay) and {form_data.get('price_accommodation_breakfast1', '')} € per night (Accommodation and Breakfast)"
                
                if check_in_month != check_out_month and check_out_date.day == 2:
                        price_info += f"\n\nThe price for a family room in the month of {check_out_month} is {form_data.get('price_stay2', '')} € per night (Only Stay) and {form_data.get('price_accommodation_breakfast2', '')} € per night (Accommodation and Breakfast)"
                
                return price_info
        @staticmethod
        def _generate_family_price_es(form_data: dict):
                check_in = form_data.get("check_in_date", "")
                check_out = form_data.get("check_out_date", "")
                
                if check_in and check_out:
                        check_in_date = datetime.strptime(check_in, "%Y-%m-%d")
                        check_out_date = datetime.strptime(check_out, "%Y-%m-%d")
                        check_in_month_en = check_in_date.strftime("%B")
                        check_out_month_en = check_out_date.strftime("%B")
                        check_in_month = month_dict.MONTHS_ES.get(check_in_month_en, check_in_month_en)
                        check_out_month = month_dict.MONTHS_ES.get(check_out_month_en, check_out_month_en)
                else:
                        check_in_month = ""
                        check_out_month = ""
                
                price_info = f"El precio de una habitación familiar en el mes de {check_in_month} es de {form_data.get('price_stay1', '')} € por noche (Solo Estancia) y {form_data.get('price_accommodation_breakfast1', '')} € por noche (Alojamiento y Desayuno)"
                
                if check_in_month != check_out_month and check_out_date.day == 2:
                        price_info += f"\n\nEl precio de una habitación familiar en el mes de {check_out_month} es de {form_data.get('price_stay2', '')} € por noche (Solo Estancia) y {form_data.get('price_accommodation_breakfast2', '')} € por noche (Alojamiento y Desayuno)"
                
                return price_info

        @staticmethod
        def _generate_apartament_price_en(form_data: dict) -> str:
                check_in = form_data.get("check_in_date", "")
                check_out = form_data.get("check_out_date", "")
                
                if check_in and check_out:
                        check_in_date = datetime.strptime(check_in, "%Y-%m-%d")
                        check_out_date = datetime.strptime(check_out, "%Y-%m-%d")
                        check_in_month = check_in_date.strftime("%B")
                        check_out_month = check_out_date.strftime("%B")
                else:
                        check_in_month = ""
                        check_out_month = ""
                
                price_info = f"The price for the apartment in the month of {check_in_month} is {form_data.get('price_stay1', '')} € per night (only stay)"
                
                if check_in_month != check_out_month and check_out_date.day == 2:
                        price_info += f"\n\nThe price for the apartment in the month of {check_out_month} is {form_data.get('price_stay2', '')} € per night (only stay)"
                
                return price_info
        
        @staticmethod
        def _generate_apartament_price_es(form_data: dict) -> str:
                check_in = form_data.get("check_in_date", "")
                check_out = form_data.get("check_out_date", "")
        
                if check_in and check_out:
                        check_in_date = datetime.strptime(check_in, "%Y-%m-%d")
                        check_out_date = datetime.strptime(check_out, "%Y-%m-%d")
                        check_in_month_en = check_in_date.strftime("%B")
                        check_out_month_en = check_out_date.strftime("%B")
                        check_in_month = month_dict.MONTHS_ES.get(check_in_month_en, check_in_month_en)
                        check_out_month = month_dict.MONTHS_ES.get(check_out_month_en, check_out_month_en)
                else:
                        check_in_month = ""
                        check_out_month = ""
                
                price_info = f"El precio del apartamento en el mes de {check_in_month} es de {form_data.get('price_stay1', '')} € por noche (solo estancia)"
                
                if check_in_month != check_out_month and check_out_date.day == 2:
                        price_info += f"\n\nEl precio del apartamento en el mes de {check_out_month} es de {form_data.get('price_stay2', '')} € por noche (solo estancia)"
                
                return price_info

        
        @staticmethod
        def double_room_template_en(form_data: dict) -> str:
                # Set a default value for rooms_to_reserve if it's not provided or is None
                rooms_to_reserve = form_data.get('rooms_to_reserve', '1')  # Default to '1' if not provided
                
                # Determine the correct word for the number of rooms
                room_word_en = "room" if rooms_to_reserve == "1" else "rooms"
                
                # Determine the correct prefix for the number of rooms
                room_prefix = "a" if rooms_to_reserve == "1" else rooms_to_reserve
                
                price_info = EmailTemplates._generate_double_price_en(form_data)
                
                check_in = form_data.get("check_in_date", "")
                check_out = form_data.get("check_out_date", "")
                
                return f"""
Dear guest,

Thank you very much for contacting us!

We are pleased to inform you that we have availability for {room_prefix} double {room_word_en} during your chosen dates:

Check-in date: {check_in} 
Check-out date: {check_out}

{price_info}

We also have superior rooms with a wonderful terrace that includes a table and two chairs. 
This type of room has an additional charge of 8 € per night. If you would like to ensure your superior room is facing Plaza de España, 
the additional charge is 10 € per night. Both room types are subject to availability, and if possible, 
we will confirm this in your booking confirmation.

To proceed with the reservation, please click on the following secure link to enter the required information:

-->> https://menahotelhub.reflex.run/hotel_reservation/ <<--

Please note that we will not charge your credit card; this is simply a guarantee for the reservation. Payment will be made upon arrival, 
and you can pay by credit card or cash.

Important: Sending the form hours or days after receiving this message does not confirm that the room has been reserved. 
You must receive a confirmation from us to ensure your booking.

If you need any additional information, please do not hesitate to contact us. We look forward to your response.

Sincerely,

{form_data.get('reception_name', '')}

Reservations Department
"""

        @staticmethod
        def double_room_template_es(form_data: dict) -> str:
                # Set a default value for rooms_to_reserve if it's not provided or is None
                rooms_to_reserve = form_data.get('rooms_to_reserve', '1')  # Default to '1' if not provided
                
                # Determine the correct word for the number of rooms
                room_word_es = "habitación" if rooms_to_reserve == "1" else "habitaciones"
                
                # Determine the correct prefix for the number of rooms
                room_prefix = "una" if rooms_to_reserve == "1" else rooms_to_reserve

                double_prefix ="doble" if rooms_to_reserve == "1" else "dobles"
                
                price_info = EmailTemplates._generate_double_price_es(form_data)
                
                check_in = form_data.get("check_in_date", "")
                check_out = form_data.get("check_out_date", "")
                return f"""
Estimado huésped,

¡Muchas gracias por contactarnos!

Nos complace informarle de que tenemos disponibilidad para {room_prefix} {room_word_es} {double_prefix} durante las fechas elegidas:

Fecha de entrada: {check_in}
Fecha de salida: {check_out}

{price_info}

También tenemos habitaciones superiores con una maravillosa terraza que incluye una mesa y dos sillas. 
Este tipo de habitación tiene un cargo adicional de 8 € por noche. Si desea asegurar que su habitación superior 
dé a la Plaza de España, el cargo adicional es de 10 € por noche. Ambos tipos de habitación están sujetos a disponibilidad, 
y si es posible, lo confirmaremos en su confirmación de reserva.

Para proceder con la reserva, por favor haga clic en el siguiente enlace seguro para ingresar la información requerida:

-->> https://menahotelhub.reflex.run/hotel_reservation/ <<--

Por favor, tenga en cuenta que no cobraremos su tarjeta de crédito; esto es simplemente una garantía para la reserva. 
El pago se realizará al llegar, y puede pagar con tarjeta de crédito o en efectivo.

Importante: Enviar el formulario horas o días después de esta comunicación no garantiza que tenga la habitación reservada. 
Deberá esperar nuestra confirmación para asegurar la reserva.

Si necesita cualquier información adicional, no dude en contactarnos. Esperamos su respuesta.

Atentamente,

{form_data.get('reception_name', '')}

Departamento de Reservas
"""


        @staticmethod
        def family_room_template_en(form_data: dict) -> str:
                # Set a default value for rooms_to_reserve if it's not provided or is None
                family_rooms_to_reserve = form_data.get('rooms_to_reserve', '1')  # Default to '1' if not provided
                
                # Determine the correct word for the number of rooms
                family_room_word_en = "room" if family_rooms_to_reserve == "1" else "rooms"
                
                # Determine the correct prefix for the number of rooms
                family_room_prefix = "a" if family_rooms_to_reserve == "1" else family_rooms_to_reserve
                
                price_info = EmailTemplates._generate_family_price_en(form_data)
                
                check_in = form_data.get("check_in_date", "")
                check_out = form_data.get("check_out_date", "")
                return f"""
Dear guest,

Thank you very much for contacting us!

We are pleased to inform you that we have availability for {family_room_prefix} family {family_room_word_en} during your chosen dates:

Check-in date: {check_in}
Check-out date: {check_out}

{price_info}

To proceed with the reservation, please click on the following secure link to enter the required information and select family room type:

-->> https://menahotelhub.reflex.run/hotel_reservation/ <<--

Please note that we will not charge your credit card; this is simply a guarantee for the reservation. Payment will be made upon arrival, 
and you can pay by credit card or cash.

Important: Sending the form hours or days after receiving this message does not confirm that the room has been reserved. 
You must receive a confirmation from us to ensure your booking.

If you need any additional information, please do not hesitate to contact us. We look forward to your response.

Sincerely,

{form_data.get('reception_name', '')}

Reservations Department
"""
        @staticmethod
        def family_room_template_es(form_data: dict) -> str:
                # Set a default value for rooms_to_reserve if it's not provided or is None
                family_rooms_to_reserve = form_data.get('rooms_to_reserve', '1')  # Default to '1' if not provided
                
                # Determine the correct word for the number of rooms
                family_room_word_es = "habitación" if family_rooms_to_reserve == "1" else "habitaciones"
                
                # Determine the correct prefix for the number of rooms
                family_room_prefix = "una" if family_rooms_to_reserve == "1" else family_rooms_to_reserve
                
                price_info = EmailTemplates._generate_family_price_es(form_data)
                
                check_in = form_data.get("check_in_date", "")
                check_out = form_data.get("check_out_date", "")
                return f"""
Estimado huésped,

¡Muchas gracias por contactarnos!

Nos complace informarle de que tenemos disponibilidad para {family_room_prefix} {family_room_word_es} familiar durante las fechas elegidas:

Fecha de entrada: {check_in}
Fecha de salida: {check_out}

{price_info}

Para proceder con la reserva, por favor haga clic en el siguiente enlace seguro para ingresar la información requerida y seleccionar el tipo de habitación familiar:

-->> https://menahotelhub.reflex.run/hotel_reservation/ <<--

Por favor, tenga en cuenta que no cobraremos su tarjeta de crédito; esto es simplemente una garantía para la reserva. El pago se realizará al llegar, y puede pagar con tarjeta de crédito o en efectivo.

Importante: Enviar el formulario horas o días después de esta comunicación no garantiza que tenga la habitación reservada. 
Deberá esperar nuestra confirmación para asegurar la reserva.

Si necesita cualquier información adicional, no dude en contactarnos. Esperamos su respuesta.

Atentamente,

{form_data.get('reception_name', '')}

Departamento de Reservas
"""

        @staticmethod
        def apartament_template_en(form_data: dict) -> str:
                # Set a default value for rooms_to_reserve if it's not provided or is None
                apartments_to_reserve = form_data.get('rooms_to_reserve', '1')  # Default to '1' if not provided
                
                # Determine the correct word for the number of rooms
                apartments_word_en = "apartment" if apartments_to_reserve == "1" else "apartments"
                
                # Determine the correct prefix for the number of rooms
                apartment_prefix = "an" if apartments_to_reserve == "1" else apartments_to_reserve
                
                price_info = EmailTemplates._generate_apartament_price_en(form_data)
                
                check_in = form_data.get("check_in_date", "")
                check_out = form_data.get("check_out_date", "")
        
                return f"""
Dear guest,

Thank you very much for contacting us!

We are pleased to inform you that we have availability for {apartment_prefix} {apartments_word_en} during your chosen dates:

Check-in date: {check_in} 
Check-out date: {check_out}

{price_info}

When booking the apartment, the first night will be charged. In case of cancellation, it is non-refundable, 
but you can modify the reservation dates until the end of 2025, depending on our availability.

To proceed with the reservation, please click on the following secure link to enter the required information and select apartment type:

-->> https://menahotelhub.reflex.run/hotel_reservation/ <<--

The apartment does not include daily cleaning.

Important: Sending the form hours or days after receiving this message does not confirm that the room has been reserved. 
You must receive a confirmation from us to ensure your booking.

If you need any additional information, please do not hesitate to contact us. We look forward to your response.

Sincerely,

{form_data.get('reception_name', '')}

Reservations Department
"""
        
        @staticmethod
        def apartament_template_es(form_data: dict) -> str:
                # Set a default value for rooms_to_reserve if it's not provided or is None
                apartments_to_reserve = form_data.get('rooms_to_reserve', '1')  # Default to '1' if not provided
                
                # Determine the correct word for the number of rooms
                apartment_word_es = "apartamento" if apartments_to_reserve == "1" else "apartamentos"
                
                # Determine the correct prefix for the number of rooms
                room_prefix = "un" if apartments_to_reserve == "1" else apartments_to_reserve
                
                price_info = EmailTemplates._generate_apartament_price_es(form_data)
                
                check_in = form_data.get("check_in_date", "")
                check_out = form_data.get("check_out_date", "")
        
                return f"""
Estimado huésped,

¡Muchas gracias por contactarnos!

Nos complace informarle de que tenemos disponibilidad para {room_prefix} {apartment_word_es} durante las fechas elegidas:

Fecha de entrada: {check_in} 
Fecha de salida: {check_out}

{price_info}

Al reservar el apartamento, se cobrará la primera noche. En caso de cancelación, no es reembolsable, 
pero puede modificar las fechas de la reserva hasta el final de 2025, dependiendo de nuestra disponibilidad.

Para proceder con la reserva, por favor haga clic en el siguiente enlace seguro para ingresar la información requerida y seleccionar el tipo de apartamento:

-->> https://menahotelhub.reflex.run/hotel_reservation/ <<--

El apartamento no incluye limpieza diaria.

Importante: Enviar el formulario horas o días después de esta comunicación no garantiza que tenga la habitación reservada. 
Deberá esperar nuestra confirmación para asegurar la reserva.

Si necesita cualquier información adicional, no dude en contactarnos. Esperamos su respuesta.

Atentamente,

{form_data.get('reception_name', '')}

Departamento de Reservas
"""