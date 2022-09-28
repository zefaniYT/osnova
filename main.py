import os.path

from flask import Flask, request, jsonify, send_from_directory

from variants.place import Country, City, Hotel
from variants.ManagerPlace import CountryManager, CityManager, HotelManager

from variants.transportation import Transport
from variants.ManagerTransport import TransportationManager

from internal.tour import Tour, SoldTours
from internal.ManagerTour import TourManager, SoldToursManager

from internal.people import Client, Payer
from internal.ManagerPeople import ClientManager, PayerManager

app = Flask(__name__)

CountryManager = CountryManager()
CityManager = CityManager()
HotelManager = HotelManager()
TransportationManager = TransportationManager()
TourManager = TourManager()
SoldToursManager = SoldToursManager()
ClientManager = ClientManager()
PayerManager = PayerManager()


@app.route("")