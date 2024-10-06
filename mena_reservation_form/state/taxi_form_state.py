import reflex as rx
import os
from dotenv import load_dotenv
from email.message import EmailMessage
import ssl
import smtplib
from urllib.parse import quote
from datetime import datetime
from mena_reservation_form.components.email_templates import EmailTemplates

class TaxiFormState(rx.State):
    
    email_sent_successfully: bool = False
    show_credit_card_numbers: bool = False

    # para controlar la activación del botón
    is_submit_enabled: bool = False  

    reservation_name: str = ""
    reservation_date:str = ""
    passenger_number:str = "" 
    flight_number:str = ""
    price:int= 0
    time_arrival:str = ""
    phone_number:str = ""
    email_address:str = ""
    observation:str = ""

    def update_submit_enabled(self):
        required_fields = [
            self.reservation_name, 
            self.reservation_date, 
            self.phone_number, 
            self.email_address, 
            self.passenger_number, 
            self.flight_number, 
            self.time_arrival
        ]
        self.is_submit_enabled = all(field != "" for field in required_fields)
            
    def set_reservation_name(self, new_name):
        self.reservation_name = new_name
        self.update_submit_enabled()

    def set_resevation_date(self, new_date):
        self.reservation_date = new_date
        self.update_submit_enabled()

    def set_passenger_number(self, new_passenger_number):
        self.passenger_number = new_passenger_number
        self.update_price()
        self.update_submit_enabled()

    def set_flight_number(self, new_flight_number):
        self.flight_number = new_flight_number
        self.update_submit_enabled()
    
    def set_time_arrival(self, new_time_arrival):
        self.time_arrival = new_time_arrival
        self.update_price()
        self.update_submit_enabled()

    def set_phone_number(self, new_phone_number):
        self.phone_number = new_phone_number
        self.update_submit_enabled()

    def set_email_address(self, new_email_address):
        self.email_address = new_email_address
        self.update_submit_enabled()

    def set_observation(self, new_observation):
        self.observation = new_observation

    def update_price(self):
        if self.passenger_number.isdigit():
            passengers = int(self.passenger_number)
            try:
                arrival_hour = int(self.time_arrival.split(':')[0])
                if 6 <= arrival_hour < 23:
                    if passengers >= 1 and passengers <= 4:
                        self.price = 75
                    elif passengers >= 5 and passengers <= 7:
                        self.price = 115
                    elif passengers >= 8 and passengers <= 13:
                        self.price = 120
                    elif passengers >= 14 and passengers <= 18:
                        self.price = 150
                else:
                    if passengers >= 1 and passengers <= 4:
                        self.price = 85
                    elif passengers >= 5 and passengers <= 7:
                        self.price = 125
                    elif passengers >= 8 and passengers <= 13:
                        self.price = 130
                    elif passengers >= 14 and passengers <= 18:
                        self.price = 160
            except ValueError:
                self.price = 0  # Valor por defecto si no se puede parsear la hora
        else:
            self.price = 0  # Valor por defecto si el número de pasajeros no es válido
    
    # Función para enviar el email
    def send_email(self): 
        load_dotenv()  
        
        # URL de la imagen
        image_url = 'https://mena-reservation-form.reflex.run/logo_letra_plateado.png'
        
        # Formatear la fecha de reserva
        reservation_date_formatted = datetime.strptime(self.reservation_date, '%Y-%m-%d').strftime('%d-%m-%Y')

        # formar email de confirmación
        email_body_en = EmailTemplates.get_taxi_confirmation_en(self.reservation_date, self.time_arrival, self.reservation_name, self.price)
        email_body_es = EmailTemplates.get_taxi_confirmation_en(self.reservation_date, self.time_arrival, self.reservation_name, self.price)

        # codificar el cuerpo del email para incluirlo en el mailto link
        email_encoded_taxi_en = quote(email_body_en)
        email_encoded_taxi_es = quote(email_body_es)

        # datos para el mailto link
        mailto_link_taxi_en = f'mailto:{self.email_address}?subject=Taxi Confirmation%20{reservation_date_formatted}%20{self.time_arrival}&body={email_encoded_taxi_en}'
        mailto_link_taxi_es = f'mailto:{self.email_address}?subject=Confirmación Taxi%20{reservation_date_formatted}%20{self.time_arrival}&body={email_encoded_taxi_es}'

        # llamada a la función de EmailTemplates para generar el html de confirmación del taxi
        content = EmailTemplates.get_email_confirmation_taxi_template(
            image_url = image_url,
            reservation_name = self.reservation_name,
            reservation_date_formatted = self.reservation_date,
            phone_number = self.phone_number,
            email_address= self.email_address,
            passenger_number = self.passenger_number,
            flight_number = self.flight_number,
            time_arrival = self.time_arrival,
            price = self.price,
            observation = self.observation,
            mailto_link_taxi_en = mailto_link_taxi_en,
            mailto_link_taxi_es= mailto_link_taxi_es
        )
        
        sender_email = os.getenv("EMAIL_SENDER")
        password = os.getenv("PASSWORD")  
        destiny = os.getenv("EMAIL_DESTINY") 
        subject = f"Formulario Reserva Taxi: {self.reservation_name}"
        body = content
        em = EmailMessage()

        em["From"] = sender_email
        em["To"] = destiny
        em["Subject"] = subject
        em.set_content(body, subtype='html')  

        context = ssl.create_default_context()  
        with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as smtp:
            smtp.login(sender_email, password)
            smtp.send_message(em)  
            self.email_sent_successfully = True
    
    def success_message(self):
        return rx.cond(
            self.email_sent_successfully,
        )

    def handle_send_taxi_email_and_message(self, FORM_DATA):
    # Actualizar los datos del estado con los valores del formulario
        self.set_reservation_name(FORM_DATA.get('reservation_name', self.reservation_name))
        self.set_resevation_date(FORM_DATA.get('reservation_date', self.reservation_date))
        self.set_phone_number(FORM_DATA.get('phone_number', self.phone_number))
        self.set_email_address(FORM_DATA.get('email_address', self.email_address))
        self.set_passenger_number(FORM_DATA.get('passenger_number', self.passenger_number))
        self.set_flight_number(FORM_DATA.get('flight_number', self.flight_number))
        self.set_time_arrival(FORM_DATA.get('arrival_time', self.time_arrival))
        self.set_observation (FORM_DATA.get('observation', self.observation))

    # Enviar el correo electrónico
        self.send_email()

    # Redirigir a la pantalla de confirmación si el correo se envió correctamente
        if self.email_sent_successfully:
            return rx.redirect("/confirmation_screen")

    # Restablecer los datos del formulario a sus valores por defecto
        self.reservation_name = ""
        self.reservation_date = ""
        self.flight_number = ""
        self.time_arrival = ""
        self.phone_number = ""
        self.email_adress = ""
        self.passenger_number = ""
        self.observation = ""
        self.price = 0


