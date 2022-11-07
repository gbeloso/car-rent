from datetime import date
class Car:
    def __init__(self, brand, model, year, day_tax):
        self.brand = brand
        self.model = model
        self.year = year
        self.day_tax = day_tax

    def consult_rent(self, date_init, date_final):
        di = date.fromisoformat(date_init)
        df = date.fromisoformat(date_final)
        return((df-di).days * self.day_tax * 1.15)