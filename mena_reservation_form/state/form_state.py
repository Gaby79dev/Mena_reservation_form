import reflex as rx
import os
from dotenv import load_dotenv
from email.message import EmailMessage
import ssl
import smtplib

class ReservationFormState(rx.State):
    
    email_sent_successfully: bool = False
    show_credit_card_numbers: bool = False

    # para controlar la activación del botón
    is_submit_enabled: bool = False  

    reservation_name: str = "" 
    check_in: str = ""
    check_out: str = ""
    phone_number:str = ""
    email_adress:str = ""
    accommodation_type:str = ""
    credit_card_number: str = ""
    expiration_date: str = ""
    observation:str = ""

    def update_submit_enabled(self):
        required_fields = [self.reservation_name, self.check_in, self.check_out, self.phone_number, self.accommodation_type, self.credit_card_number, self.expiration_date]
        self.is_submit_enabled = all(field != "" for field in required_fields)

    def set_accommodation_type(self, new_accomodation_type):
        self.accommodation_type = new_accomodation_type
        self.update_submit_enabled()

    def set_show_credit_card_numbers(self, new_value):
        self.show_credit_card_numbers = new_value
        self.update_submit_enabled()
    
    def toggle_show_numbers(self, checked: bool):
        self.show_credit_card_numbers = checked
            

    def set_reservation_name(self, new_name):
        self.reservation_name = new_name
        self.update_submit_enabled()

    def set_check_in(self,new_check_in):
        self.check_in = new_check_in
        self.update_submit_enabled()

    def set_check_out(self,new_check_out):
        self.check_out = new_check_out
        self.update_submit_enabled()

    def set_phone_number(self, new_phone_number):
        self.phone_number = new_phone_number
        self.update_submit_enabled()

    def set_email_adress(self, new_email_adress):
        self.email_adress = new_email_adress

    def set_credit_card_number(self, new_credit_card_number):
        self.credit_card_number = new_credit_card_number
        self.update_submit_enabled()
    
    def set_expiration_date(self, new_expiration_date):
        self.expiration_date = new_expiration_date
        self.update_submit_enabled()

    def set_observation(self, new_observation):
        self.observation = new_observation

    def send_email(self): 
        load_dotenv()  
        content = f"<p>Reserva de: {self.reservation_name}</p>"
        content += f"<p>Fecha de entrada: {self.check_in}</p>"
        content += f"<p>Fecha de salida: {self.check_out}</p>"
        content += f"<p>Nº Teléfono: {self.phone_number}</p>"
        content += f"<p>Email: {self.email_adress}</p>"
        content += f"<p>Tipo de Alojamiento: {self.accommodation_type}</p>"
        content += f"<p>Número de tc: {self.credit_card_number}</p>"
        content += f"<p>Fecha de tc: {self.expiration_date}</p>"
        content += f"<p>Observaciones: {self.observation}</p>"

        sender_email = os.getenv("EMAIL_SENDER")
        password = os.getenv("PASSWORD")  
        destiny = os.getenv("EMAIL_DESTINY") 
        subject = f"Formulario Reserva: {self.reservation_name}"
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
            rx.text("Correo enviado con éxito!", color="green", align="center"),
            
        )

    def handle_send_email_and_message(self, FORM_DATA):
    # Actualizar los datos del estado con los valores del formulario
        self.set_reservation_name(FORM_DATA.get('reservation_name', self.reservation_name))
        self.set_check_in(FORM_DATA.get('check_in', self.check_in))
        self.set_check_out(FORM_DATA.get('check_out', self.check_out))
        self.set_phone_number(FORM_DATA.get('phone_number', self.phone_number))
        self.set_email_adress(FORM_DATA.get('email_adress', self.email_adress))
        self.set_accommodation_type(FORM_DATA.get('accommodation_type', self.accommodation_type))
        self.set_credit_card_number(FORM_DATA.get('credit_card_number', self.credit_card_number))
        self.set_expiration_date(FORM_DATA.get('expiration_date', self.expiration_date))
        self.set_observation (FORM_DATA.get('observation', self.observation))

    # Enviar el correo electrónico
        self.send_email()

    # Mostrar mensaje de éxito si el correo se envió correctamente
        self.success_message()

    # Restablecer los datos del formulario a sus valores por defecto
        self.reservation_name = ""
        self.check_in = ""
        self.check_out = ""
        self.phone_number = ""
        self.email_adress = ""
        self.accommodation_type = ""
        self.credit_card_number = ""
        self.expiration_date = ""
        
        



