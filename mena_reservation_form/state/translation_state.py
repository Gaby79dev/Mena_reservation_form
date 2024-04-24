import reflex as rx

# Definimos una clase para las traducciones que herede de rx.Base
class Translations(rx.Base):
    en: dict = {
        'reservation_form': 'Reservation Form',
        'reservation_name': 'Reservation Name:',
        'reservation_check_in': 'Check in:',
        'reservation_check_out': 'Check out:',
        'reservation_phone_number':'Phone number:',
        'reservation_email_adress':'Email adress:',
        'reservation_accommodation_Type':'Accomm. Type:',
        'reservation_show_numbers': 'Show numbers:',
        'reservation_card_number': 'Credit card nº:',
        'reservation_expirate_date': 'Expirate date:',
        'reservation_observation': 'Observations:',
        # Texto del botón en inglés.
        'reservation_button_submit': 'Submit',
        # Para las traducciones de las variables del rx.select(menú desplegable)
        'reservation_only_stay': 'Only stay',
        'reservation_breakfast_stay': 'Bed and breakfast',
    }
    es: dict = {
        'reservation_form': 'Formulario de Reserva',
        'reservation_name': 'Nombre reserva:',
        'reservation_check_in': 'Fecha entrada:',
        'reservation_check_out': 'Fecha salida:',
        'reservation_accommodation_Type':'Tipo Estancia:',
        'reservation_phone_number':'Nº Teléfono:',
        'reservation_email_adress':'Email:',
        'reservation_show_numbers': 'Mostrar números:',
        'reservation_card_number': 'Nº Tarjeta crédito:',
        'reservation_expirate_date': 'Fecha caducidad:',
        'reservation_observation': 'Observaciones:',
        # texto del botón en español
        'reservation_button_submit': 'Enviar',
        # Para las traducciones de las variables del rx.select(menú desplegable)
        'reservation_only_stay': 'Sólo Alojamiento',
        'reservation_breakfast_stay': 'Alojamiento y desayuno',
    }

# Adaptamos la clase Translation_state para utilizar la nueva estructura de datos
class Translation_state(rx.State):
    current_language: str = 'en'  # Idioma por defecto
    translations: Translations = Translations()  # Instancia de la clase Translations
    # Agrego una nueva variable de estado para la traducción del formulario
    reservation_form_translation: str = 'Reservation Form'  # Valor inicial
    reservation_form_translation_name: str = 'Reservation Name'
    reservation_form_translation_check_in: str = 'Check in'
    reservation_form_translation_check_out: str = 'Check out'
    reservation_form_translation_phone_number:str = 'Phone number'
    reservation_form_translation_email_adress:str = 'Email adress'
    reservation_form_tranlation_show_numbers: str = 'Show numbers'
    reservation_form_translation_card_number: str = 'Credit card nº'
    reservation_form_translation_expirate_date: str = 'Expirate date'
    reservation_form_translation_observation:str = 'Observations'
    reservation_form_translation_accommodation_type:str = 'Accomm. Type'
    reservation_form_translation_only_stay:str = 'Only stay'
    reservation_form_translation_breakfast_stay: str = 'Bed and breakfast'
    reservation_form_translation_button_submit:str = 'Submit'




    def set_language(self, lang: str):
        self.current_language = lang
        # Actualizo la traducción del formulario de reserva
        self.reservation_form_translation = self.translate('reservation_form')
        self.reservation_form_translation_name = self.translate('reservation_name')
        self.reservation_form_translation_check_in = self.translate('reservation_check_in')
        self.reservation_form_translation_check_out = self.translate('reservation_check_out')
        self.reservation_form_translation_phone_number = self.translate('reservation_phone_number')
        self.reservation_form_translation_email_adress = self.translate('reservation_email_adress')
        self.reservation_form_translation_show_numbers = self.translate('reservation_show_numbers')
        self.reservation_form_translation_card_number = self.translate('reservation_card_number')
        self.reservation_form_translation_expirate_date = self.translate('reservation_expirate_date')
        self.reservation_form_translation_observation = self.translate('reservation_observation')
        self.reservation_form_translation_accommodation_type = self.translate('reservation_accommodation_Type')
        self.reservation_form_translation_only_stay = self.translate('reservation_only_stay')
        self.reservation_form_translation_breakfast_stay = self.translate('reservation_breakfast_stay')
        self.reservation_form_translation_button_submit= self.translate('reservation_button_submit')


    def translate(self, key: str) -> str:
        """Obtiene la traducción para la clave dada basándose en el idioma actual."""
        # Accedemos al diccionario de traducciones para el idioma actual
        # y retornamos el valor para la clave solicitada.
        return self.translations.__getattribute__(self.current_language)[key]