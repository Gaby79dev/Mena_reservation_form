import reflex as rx

class NavigationState(rx.State):
    
    def navigate_to_index(self):
        return rx.redirect('/')
    
    def navigate_to_dashboard(self):
        return rx.redirect("/dashboard")
    
    def navigate_to_room_templates(self):
        return rx.redirect('/room_templates')
    
    def navigate_to_hotel_form(self):
        return rx.redirect('/hotel_reservation')
    
    def navigate_to_taxi_form(self):
        return rx.redirect('/taxi_reservation')
    
    def navigate_to_confirmation_screen(self):
        return rx.redirect('/confirmation_screen')
    
    def navigate_to_login_screen(self):
        return rx.redirect('/login_screen')
    
