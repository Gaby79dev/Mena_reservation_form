import reflex as rx
from mena_reservation_form.components.email_templates import EmailTemplates
from datetime import datetime

class ReservationTemplateState(rx.State):
    form_data: dict = {}
    is_submit_enabled: bool = False
    current_template: str = "double_room"
    show_additional_prices: bool = False
    selected_template: str = "double_room"
    current_form: str = "reservation"  # Nuevo estado para controlar el formulario actual

    def handle_submit(self, form_data: dict):
        """Handle the form submit."""
        self.form_data = form_data
        
        # Aplicar descuentos
        if self.form_data.get("price_genius") and self.form_data.get("price_long_stay"):
            self.apply_discount("price_stay1", 0.85)  # 15% de descuento
            if "price_stay2" in self.form_data:
                self.apply_discount("price_stay2", 0.85)
            if "price_accommodation_breakfast1" in self.form_data:
                self.apply_discount("price_accommodation_breakfast1", 0.85)
            if "price_accommodation_breakfast2" in self.form_data:
                self.apply_discount("price_accommodation_breakfast2", 0.85)
        else:
            if self.form_data.get("price_genius"):
                self.apply_discount("price_stay1", 0.9)  # 10% de descuento
                if "price_stay2" in self.form_data:
                    self.apply_discount("price_stay2", 0.9)
                if "price_accommodation_breakfast1" in self.form_data:
                    self.apply_discount("price_accommodation_breakfast1", 0.9)
                if "price_accommodation_breakfast2" in self.form_data:
                    self.apply_discount("price_accommodation_breakfast2", 0.9)
            
            if self.form_data.get("price_long_stay"):
                self.apply_discount("price_stay1", 0.95)  # 5% de descuento
                if "price_stay2" in self.form_data:
                    self.apply_discount("price_stay2", 0.95)
                if "price_accommodation_breakfast1" in self.form_data:
                    self.apply_discount("price_accommodation_breakfast1", 0.95)
                if "price_accommodation_breakfast2" in self.form_data:
                    self.apply_discount("price_accommodation_breakfast2", 0.95)

    def apply_discount(self, price_field: str, discount_factor: float):
        if price_field in self.form_data and self.form_data[price_field] is not None and self.form_data[price_field] != '':
            try:
                self.form_data[price_field] = round(float(self.form_data[price_field]) * discount_factor, 2)
            except ValueError:
                print(f"Error: Could not convert {price_field} value to float.")

    def update_dates(self, value: str, is_check_in: bool):
        if is_check_in:
            self.form_data["check_in_date"] = value
        else:
            self.form_data["check_out_date"] = value
        
        check_in = self.form_data.get("check_in_date", "")
        check_out = self.form_data.get("check_out_date", "")
        
        if check_in and check_out:
            check_in_date = datetime.strptime(check_in, "%Y-%m-%d")
            check_out_date = datetime.strptime(check_out, "%Y-%m-%d")
            self.show_additional_prices = check_in_date.month != check_out_date.month
        else:
            self.show_additional_prices = False

    @rx.var
    def formatted_check_in_date(self) -> rx.Component:
        return rx.moment(self.form_data.get("check_in_date", ""), format="DD/MM/YYYY")

    @rx.var
    def formatted_check_out_date(self) -> rx.Component:
        return rx.moment(self.form_data.get("check_out_date", ""), format="DD/MM/YYYY")

    def set_template(self, template_name: str):
        self.selected_template = template_name  
        if template_name == "double_room_es":
            self.current_template = EmailTemplates.double_room_template_es(self.form_data)
        elif template_name == "double_room":
            self.current_template = EmailTemplates.double_room_template_en(self.form_data)
        elif template_name == "family_room_es":
            self.current_template = EmailTemplates.family_room_template_es(self.form_data)
        elif template_name == "family_room":
            self.current_template = EmailTemplates.family_room_template_en(self.form_data)
        elif template_name == "apartment_es":
            self.current_template = EmailTemplates.apartament_template_es(self.form_data)
        elif template_name == "apartment":
            self.current_template = EmailTemplates.apartament_template_en(self.form_data)
        elif template_name == "taxi":
            self.current_template = "taxi"

    @rx.var
    def email_preview(self) -> str:
        if self.selected_template == "double_room_es":
            return EmailTemplates.double_room_template_es(self.form_data)
        elif self.selected_template == "double_room":
            return EmailTemplates.double_room_template_en(self.form_data)
        elif self.selected_template == "family_room_es":
            return EmailTemplates.family_room_template_es(self.form_data)
        elif self.selected_template == "family_room":
            return EmailTemplates.family_room_template_en(self.form_data)
        elif self.selected_template == "apartment_es":
            return EmailTemplates.apartament_template_es(self.form_data)
        elif self.selected_template == "apartment":
            return EmailTemplates.apartament_template_en(self.form_data)
        else:
            return EmailTemplates.double_room_template_en(self.form_data)
        
    @rx.var
    def header_text(self) -> str:
        if self.selected_template == "double_room_es":
            return "Plantilla habitación doble (Español)"
        elif self.selected_template == "double_room":
            return "Plantilla habitación doble"
        elif self.selected_template == "family_room_es":
            return "Plantilla habitación familiar (Español)"
        elif self.selected_template == "family_room":
            return "Plantilla habitación familiar"
        elif self.selected_template == "apartment_es":
            return "Plantilla apartamento (Español)"
        elif self.selected_template == "apartment":
            return "Plantilla apartamento"
        else:
            return "Plantilla habitación doble"
        
    def copy_template(self):
        return rx.set_clipboard(self.email_preview)