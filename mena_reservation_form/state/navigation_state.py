import reflex as rx

class NavigationState(rx.State):
    
    def navigate_to_index(self):
        return rx.redirect('/')
    
    def navigate_to_taxi_form(self):
        return rx.redirect('/taxi_reservation')
    
    def navigate_to_confirmation_screen(self):
        return rx.redirect('/confirmation_screen')
    