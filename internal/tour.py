class Tour:
    def __init__(self, hotel_id, transportation_id, price, name, days, Departure_date, Arrival_date, id=None):
        self.hotel_id = hotel_id
        self.transportation_id = transportation_id
        self.price = price
        self.days = days
        self.Departure_date = Departure_date
        self.Arrival_date = Arrival_date
        self.name = name
        self.id = id
class SoldTours:
    def __init__(self, price, tur_id, client_id, payer_id, data, id):
        self.price = price
        self.tur_id = tur_id
        self.client_id = client_id
        self.payer_id = payer_id
        self.data = data
        self.id = id
