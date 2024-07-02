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
        'reservation_accommodation_Type':'Stay options:',
        'reservation_show_numbers': 'Show numbers:',
        'reservation_card_number': 'Credit card nº:',
        'reservation_expirate_date': 'Expirate date:',
        'reservation_observation': 'Observations:',
        'taxi_reservation_title': 'Taxi Reservation',
        'taxi_reservation_name' : 'Reservation Name:',
        'taxi_flight_number': 'Flight Number:',
        'taxi_arrival_time': 'Arrival Time:',
        'taxi_arrival_date': 'Reservation Date:',
        'taxi_passenger_number':'Number of Passenger:',
        'taxi_price' : 'PRICE',

        # Texto del botón en inglés.
        'reservation_button_submit': 'Submit',
        # Para las traducciones de las variables del rx.select(menú desplegable)
        'reservation_only_stay': 'Only stay',
        'reservation_breakfast_stay': 'Bed and breakfast',
        # texto para "campos obligatorios
        'mandatory_fields' : '- Mandatory Fields *',
        # texto para la política de privacidad
        'responsible' : '- Responsible: ANGESGAR S.L',
        'purpose' : '- Purpose: Manage your request.',
        'legitimacy' : '- Legitimacy: Your consent for the purpose described.',
        'recipients' : '- Recipients: Data will not be transferred to third parties.',
        'rights':'- Rights: You can access, rectify, and delete your data.',
        # texto tipo de habitación (standar, Superior, Superior a la plaza)
        'room_type':'Room Type:',
        'standar':'Standar room',
        'superior':'Superior room--8€ per night.',
        'superior_facing':'Superior room Square--10€ per night.',
        'family_room':'Family room--4 pax.',
        'apartment':'Apartment--4 pax.',
        # dropdownMenu de los números de habitaciones
        'rooms_to_reserve':'Rooms to Reserve:',
        'one':'one',
        'two':'two',
        'three':'three',
        'four':'four',
        'five':'five',
        'six':'six',
        'seven':'seven',
        'eight':'eight',
        'nine':'nine',
        'ten':'ten',

    }
    es: dict = {
        'reservation_form': 'Formulario de Reserva',
        'reservation_name': 'Nombre reserva:',
        'reservation_check_in': 'Fecha entrada:',
        'reservation_check_out': 'Fecha salida:',
        'reservation_accommodation_Type':'En régimen:',
        'reservation_phone_number':'Nº Teléfono:',
        'reservation_email_adress':'Email:',
        'reservation_show_numbers': 'Mostrar números:',
        'reservation_card_number': 'Nº Tarjeta crédito:',
        'reservation_expirate_date': 'Fecha caducidad:',
        'reservation_observation': 'Observaciones:',
        'taxi_reservation_title': 'Reserva de Taxi',
        'taxi_reservation_name' : 'Nombre de Reserva:',
        'taxi_flight_number': 'Número de Vuelo:',
        'taxi_arrival_time': 'Hora de llegada:',
        'taxi_arrival_date': 'Fecha de Reserva:',
        'taxi_passenger_number':'Número de Pasajeros:',
        'taxi_price':'PRECIO',

        # texto del botón en español
        'reservation_button_submit': 'Enviar',
        # Para las traducciones de las variables del rx.select(menú desplegable)
        'reservation_only_stay': 'Sólo Alojamiento',
        'reservation_breakfast_stay': 'Alojamiento y desayuno',
        # texto para "campos obligatorios
        'mandatory_fields' : '- campos obligatorios *', 
        # texto para la política de privacidad
        'responsible' : '- Responsable: ANGESGAR S.L',
        'purpose' : '- Finalidad: Gestionar su solicitud',
        'legitimacy' : '- Legitimación: Su consentimiento para la finalidad descrita.',
        'recipients' : '- Destinatarios: No se cederán datos a terceros.',
        'rights' : '- Derechos: Puede acceder, rectificar y suprimir sus datos.',
        # texto tipo de habitación (standar, Superior, Superior a la plaza)
        'room_type':'Tipo de habitación',
        'standar':'Doble Estandar.',
        'superior':'Doble Superior--8€ por noche.',
        'superior_facing':'Doble Superior a la plaza--10€ por noche.',
        'family_room':'Habitación familiar--4 pax.',
        'apartment':'Apartamento--4 pax.',
        # dropdownMenu de los números de habitaciones
        'rooms_to_reserve':'Nº habitaciones:',
        'one':'una',
        'two':'dos',
        'three':'tres',
        'four':'cuatro',
        'five':'cinco',
        'six':'seis',
        'seven':'siete',
        'eight':'oche',
        'nine':'nueve',
        'ten':'diez',
        
    }

# Adaptamos la clase Translation_state para utilizar la nueva estructura de datos
class Translation_state(rx.State):
    current_language: str = 'en'  # Idioma por defecto
    translations: Translations = Translations()  # Instancia de la clase Translations
    # Agrego una nueva variable de estado para la traducción del formulario
    reservation_form_translation: str = 'RESERVATION FORM'  # Valor inicial
    reservation_form_translation_name: str = 'Reservation Name:'
    reservation_form_translation_check_in: str = 'Check in:'
    reservation_form_translation_check_out: str = 'Check out:'
    reservation_form_translation_phone_number:str = 'Phone number:'
    reservation_form_translation_email_adress:str = 'Email adress:'
    reservation_form_tranlation_show_numbers: str = 'Show numbers:'
    reservation_form_translation_card_number: str = 'Credit card nº:'
    reservation_form_translation_expirate_date: str = 'Expirate date:'
    reservation_form_translation_observation:str = 'Observations:'
    reservation_form_translation_accommodation_type:str = 'Stay options:'
    reservation_form_translation_only_stay:str = 'Only stay'
    reservation_form_translation_breakfast_stay: str = 'Bed and breakfast'
    reservation_form_translation_button_submit:str = 'Submit'
    reservation_form_translation_taxi_title = 'TAXI RESERVATION'
    reservation_form_tranlation_taxi_name = 'Reservation Name:'
    reservation_form_translation_taxi_flight_number = 'Flight Number:'
    reservation_form_translation_taxi_arrival_time = 'Arrival Time:'
    reservation_form_translation_taxi_arrival_date = 'Reservation Date:'
    reservation_form_translation_passenger_number = 'Number of Passenger:'
    reservation_form_translation_taxi_price = 'PRICE'
    reservation_form_translation_mandatory_field = '- mandatory fields *'
    reservation_form_responsible = '- Responsible: ANGESGAR S.L'
    reservation_form_purpose = '- Purpose: Manage your request.'
    reservation_form_legitimacy = '- Legitimacy: Your consent for the purpose described.'
    reservation_form_recipients = '- Recipients: Data will not be transferred to third parties.'
    reservation_form_rights = '- Rights: You can access, rectify, and delete your data, as well as other rights, as explained in the additional information.'
    reservation_form_translation_room_type = 'Room Type'
    reservation_form_translation_standar_room = 'Standar double room'
    reservation_form_translation_superior_room = 'Superior double room--8€ per night.'
    reservation_form_translation_superior_room_square = 'Superior double room Square--10€ per night.'
    reservation_form_translation_family_room: str = 'Family Room--4 pax'
    reservation_form_translation_apartment: str = 'Apartment--4 pax'
    reservation_form_translation_rooms_to_reserve: str = 'Rooms to Reserve'
    reservation_form_translation_rooms_to_reserve_one:str = 'one'
    reservation_form_translation_rooms_to_reserve_two: str = 'two'
    reservation_form_translation_rooms_to_reserve_three: str = 'three'
    reservation_form_translation_rooms_to_reserve_four: str = 'four'
    reservation_form_translation_rooms_to_reserve_five: str = 'five'
    reservation_form_translation_rooms_to_reserve_six: str = 'six'
    reservation_form_translation_rooms_to_reserve_seven: str = 'seven'
    reservation_form_translation_rooms_to_reserve_eight: str = 'eight'
    reservation_form_translation_rooms_to_reserve_nine: str = 'nine'
    reservation_form_translation_rooms_to_reserve_ten: str = 'ten'
    
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
        self.reservation_form_translation_taxi_title = self.translate('taxi_reservation_title')
        self.reservation_form_translation_taxi_name = self.translate('taxi_reservation_name')
        self.reservation_form_translation_taxi_flight_number = self.translate('taxi_flight_number')
        self.reservation_form_translation_taxi_arrival_time = self.translate('taxi_arrival_time')
        self.reservation_form_translation_taxi_arrival_date= self.translate('taxi_arrival_date')
        self.reservation_form_translation_passenger_number = self.translate('taxi_passenger_number')
        self.reservation_form_translation_taxi_price = self.translate('taxi_price')
        self.reservation_form_translation_mandatory_field = self.translate('mandatory_fields')
        self.reservation_form_responsible = self.translate('responsible')
        self.reservation_form_purpose=self.translate('purpose')
        self.reservation_form_legitimacy=self.translate('legitimacy')
        self.reservation_form_recipients = self.translate('recipients')
        self.reservation_form_rights=self.translate('rights')
        self.reservation_form_translation_room_type = self.translate('room_type')
        self.reservation_form_translation_standar_room = self.translate('standar')
        self.reservation_form_translation_superior_room = self.translate('superior')
        self.reservation_form_translation_superior_room_square =  self.translate('superior_facing')
        self.reservation_form_translation_family_room = self.translate('family_room')
        self.reservation_form_translation_apartment = self.translate('apartment')
        self.reservation_form_translation_rooms_to_reserve = self.translate('rooms_to_reserve')
        self.reservation_form_translation_rooms_to_reserve_one = self.translate('one')
        self.reservation_form_translation_rooms_to_reserve_two = self.translate('two')
        self.reservation_form_translation_rooms_to_reserve_three = self.translate('three')
        self.reservation_form_translation_rooms_to_reserve_four = self.translate('four')
        self.reservation_form_translation_rooms_to_reserve_five = self.translate('five')
        self.reservation_form_translation_rooms_to_reserve_six = self.translate('six')
        self.reservation_form_translation_rooms_to_reserve_seven = self.translate('seven')
        self.reservation_form_translation_rooms_to_reserve_eight = self.translate('eight')
        self.reservation_form_translation_rooms_to_reserve_nine = self.translate('nine')
        self.reservation_form_translation_rooms_to_reserve_ten = self.translate('ten')



    def translate(self, key: str) -> str:
        """Obtiene la traducción para la clave dada basándose en el idioma actual."""
        # Accedemos al diccionario de traducciones para el idioma actual
        # y retornamos el valor para la clave solicitada.
        return self.translations.__getattribute__(self.current_language)[key]
    
    