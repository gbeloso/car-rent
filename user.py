class User:
    def __init__(self, name, email, password):
        self.name = name
        self.email = email
        self.password = password
    
    def rent_car(self, car, date_init, date_final):
        self.rented_car = car
        self.date_init = date_init
        self.date_final = date_final