class Tour:
    def Tour(self, hotel_id, transportation_id, price, name, id=None):
        self.city_id = hotel_id
        self.stars = transportation_id
        self.price = price
        self.name = name
        self.id = id