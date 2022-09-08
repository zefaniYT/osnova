class Country:
    def __init__(self, name, id=None):
        self.id = id
        self.name = name

class City:
    def __init__(self, country_id, name, id = None):
        self.country_id = country_id
        self.id = id
        self.name = name

class Hotel:
    def __init__(self, city_id, stars, price, name, id=None):
        self.city_id = city_id
        self.stars = stars
        self.price = price
        self.name = name
        self.id = id

