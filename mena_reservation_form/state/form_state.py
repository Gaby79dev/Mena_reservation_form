import reflex as rx
import os
from dotenv import load_dotenv
from email.message import EmailMessage
import ssl
import smtplib
from datetime import datetime
from urllib.parse import quote
from mena_reservation_form.components.email_templates import EmailTemplates
from babel.dates import format_date, Locale
import re


class ReservationFormState(rx.State):
    email_sent_successfully: bool = False
    show_credit_card_numbers: bool = False
    is_submit_enabled: bool = False  # Para controlar la activación del botón

    reservation_name: str = "" 
    check_in: str = ""
    check_out: str = ""
    phone_number: str = ""
    email_address: str = ""
    accommodation_type: str = ""
    rooms_to_reserve: str = ""
    superior_type: str = ""
    credit_card_number: str = ""
    expiration_date: str = ""
    observation: str = ""

    def update_submit_enabled(self):
        # Actualiza el estado del botón de envío basado en campos requeridos
        required_fields = [
            self.reservation_name, self.check_in, self.check_out, 
            self.phone_number, self.accommodation_type, self.superior_type,
            self.rooms_to_reserve, self.credit_card_number, self.expiration_date
        ]
        self.is_submit_enabled = all(field != "" for field in required_fields)
    
    def set_rooms_to_reserve(self, new_rooms_to_reserve):
        self.rooms_to_reserve = new_rooms_to_reserve
        self.update_submit_enabled()
    
    def set_superior_type(self, new_superior_type):
        self.superior_type = new_superior_type
        self.update_submit_enabled()

    def set_accommodation_type(self, new_accommodation_type):
        self.accommodation_type = new_accommodation_type
        self.update_submit_enabled()

    def set_show_credit_card_numbers(self, new_value):
        self.show_credit_card_numbers = new_value
        self.update_submit_enabled()
    
    def toggle_show_numbers(self, checked: bool):
        self.show_credit_card_numbers = checked            

    def set_reservation_name(self, new_name):
        self.reservation_name = new_name
        self.update_submit_enabled()

    def set_check_in(self, new_check_in):
        self.check_in = new_check_in
        self.update_submit_enabled()

    def set_check_out(self, new_check_out):
        self.check_out = new_check_out
        self.update_submit_enabled()

    def set_phone_number(self, new_phone_number):
        self.phone_number = new_phone_number
        self.update_submit_enabled()

    def set_email_address(self, new_email_address):
        self.email_address = new_email_address

    def set_credit_card_number(self, new_credit_card_number):
        # Eliminar cualquier carácter no numérico y asegurarse de que solo queden 16 dígitos
        cleaned_number = ''.join(filter(str.isdigit, new_credit_card_number))
        if len(cleaned_number) > 16:
            cleaned_number = cleaned_number[:16]
        self.credit_card_number = cleaned_number
        self.update_submit_enabled()

    def format_credit_card_number(self, credit_card_number):
        # Utiliza una expresión regular para formatear el número de tarjeta de crédito
        return ' '.join(re.findall('.{1,4}', credit_card_number))
    
    def set_expiration_date(self, new_expiration_date):
        self.expiration_date = new_expiration_date
        self.update_submit_enabled()

    def set_observation(self, new_observation):
        self.observation = new_observation

    def get_month_from_date(self, date_str):  # Establece el valor predeterminado en inglés
        try:
            date_obj = datetime.strptime(date_str, '%d-%m-%Y')
        except ValueError:
            raise ValueError(f"Formato de fecha inválido: {date_str}")

        locale_en = Locale.parse('en')
        locale_es = Locale.parse('es')

        month_name_en = format_date(date_obj, format='MMMM', locale=locale_en)
        month_name_es = format_date(date_obj, format='MMMM', locale=locale_es)

        return {'en': month_name_en, 'es': month_name_es}

    def send_email(self): 
        load_dotenv() 

        # URL de la imagen
        image_url = 'https://mena-reservation-form.reflex.run/logo_letra_plateado.png'

        # Formatea las fechas para el correo electrónico
        check_in_date = datetime.strptime(self.check_in, '%Y-%m-%d').strftime('%d-%m-%Y')
        check_out_date = datetime.strptime(self.check_out, '%Y-%m-%d').strftime('%d-%m-%Y')

        # Formatea el número de tarjeta de crédito
        formatted_credit_card_number = self.format_credit_card_number(self.credit_card_number)

        # Obtiene el nombre del mes en español e inglés
        month_names = self.get_month_from_date(check_in_date)
        month_en = month_names['en']
        month_es = month_names['es']
            
        email_body_double_en = EmailTemplates.get_email_template_double_en(
            self.reservation_name,
            check_in_date,
            check_out_date,
            self.accommodation_type,
            self.superior_type,
            self.rooms_to_reserve,
            month_en
        )
        
        email_body_double_es = EmailTemplates.get_email_template_double_es(
            self.reservation_name,
            check_in_date,
            check_out_date,
            self.accommodation_type,
            self.superior_type,
            self.rooms_to_reserve,
            month_es
        )

        email_body_family_en = EmailTemplates.get_email_template_family_en(
            self.reservation_name,
            check_in_date,
            check_out_date,
            self.accommodation_type,
            self.rooms_to_reserve,
            month_en
        )

        email_body_family_es = EmailTemplates.get_email_template_family_es(
            self.reservation_name,
            check_in_date,
            check_out_date,
            self.accommodation_type,
            self.rooms_to_reserve,
            month_es            
        )

        email_body_apartment_en = EmailTemplates.get_email_template_apartment_en(
            self.reservation_name,
            check_in_date,
            check_out_date,
            self.accommodation_type,
            month_en            
        )

        email_body_apartment_es = EmailTemplates.get_email_template_apartment_es(
            self.reservation_name,
            check_in_date,
            check_out_date,
            self.accommodation_type,
            month_es            
        )
    
        # Codificar el cuerpo del email para incluirlo en el mailto link
        email_body_encoded_double_en = quote(email_body_double_en)
        email_body_encoded_double_es = quote(email_body_double_es)
        email_body_encoded_family_en = quote(email_body_family_en)
        email_body_encoded_family_es = quote(email_body_family_es)
        email_body_encoded_apartment_en = quote(email_body_apartment_en)
        email_body_encoded_apartment_es = quote(email_body_apartment_es)

        # Datos para el mailto link
        mailto_link_double_en = f'mailto:{self.email_address}?subject=Mena Plaza Confirmation%20{check_in_date}%20To%20{check_out_date}&body={email_body_encoded_double_en}'
        mailto_link_double_es = f'mailto:{self.email_address}?subject=Confirmación Mena Plaza%20{check_in_date}%20a%20{check_out_date}&body={email_body_encoded_double_es}'
        mailto_link_family_en = f'mailto:{self.email_address}?subject=Mena Plaza Confirmation%20{check_in_date}%20To%20{check_out_date}&body={email_body_encoded_family_en}'
        mailto_link_family_es = f'mailto:{self.email_address}?subject=Confirmación Mena Plaza%20{check_in_date}%20a%20{check_out_date}&body={email_body_encoded_family_es}'
        mailto_link_apartment_en = f'mailto:{self.email_address}?subject=Mena Plaza Confirmation%20{check_in_date}%20To%20{check_out_date}&body={email_body_encoded_apartment_en}'
        mailto_link_apartment_es = f'mailto:{self.email_address}?subject=Confirmación Mena Plaza%20{check_in_date}%20a%20{check_out_date}&body={email_body_encoded_apartment_es}'

        # llamada a la función de EmailTemplates para generar el html de confirmación de la reserva
        content = EmailTemplates.get_email_confirmation_reservation_template(
                image_url, 
                reservation_name = self.reservation_name,
                check_in_date = self.check_in,
                check_out_date = self.check_out,
                phone_number = self.phone_number,
                email_address = self.email_address,
                rooms_to_reserve = self.rooms_to_reserve,
                accommodation_type = self.accommodation_type,
                superior_type = self.superior_type,
                formatted_credit_card_number = formatted_credit_card_number,
                expiration_date = self.expiration_date,
                observation = self.observation,
                mailto_link_double_en = mailto_link_double_en,
                mailto_link_double_es = mailto_link_double_es,
                mailto_link_family_en = mailto_link_family_en,
                mailto_link_family_es = mailto_link_family_es,
                mailto_link_apartment_en = mailto_link_apartment_en,
                mailto_link_apartment_es = mailto_link_apartment_es
        )
        
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
            "Email sent successfully!",
            "Failed to send email."
        )
    
    def handle_send_email_and_message(self, FORM_DATA):
        # Actualizar los datos del estado con los valores del formulario
        self.set_reservation_name(FORM_DATA.get('reservation_name', self.reservation_name))
        self.set_check_in(FORM_DATA.get('check_in', self.check_in))
        self.set_check_out(FORM_DATA.get('check_out', self.check_out))
        self.set_phone_number(FORM_DATA.get('phone_number', self.phone_number))
        self.set_email_address(FORM_DATA.get('email_address', self.email_address))
        self.set_accommodation_type(FORM_DATA.get('accommodation_type', self.accommodation_type))
        self.set_rooms_to_reserve(FORM_DATA.get('rooms_to_reserve', self.rooms_to_reserve))
        self.set_superior_type(FORM_DATA.get('superior_type', self.superior_type))
        self.set_credit_card_number(FORM_DATA.get('credit_card_number', self.credit_card_number))
        self.set_expiration_date(FORM_DATA.get('expiration_date', self.expiration_date))
        self.set_observation(FORM_DATA.get('observation', self.observation))

        # Enviar el correo electrónico
        self.send_email()

        # Redirigir a la pantalla de confirmación si el correo se envió correctamente
        if self.email_sent_successfully:
            # Restablecer los datos del formulario a sus valores por defecto
            self.reservation_name = ""
            self.check_in = ""
            self.check_out = ""
            self.phone_number = ""
            self.email_address = ""
            self.rooms_to_reserve = ""
            self.accommodation_type = ""
            self.superior_type = ""
            self.credit_card_number = ""
            self.expiration_date = ""
            self.observation = ""

            return rx.redirect("/confirmation_screen")
        
        # Si el correo no se envió correctamente, puedes manejar el error aquí
        # Por ejemplo, estableciendo un estado de error o mostrando un mensaje al usuario
        # self.email_sent_successfully = False  # Ya está establecido por defecto