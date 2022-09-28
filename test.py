from internal.ManagerTour import TourManager
from internal.tour import Tour

tour = TourManager()

tour.add(Tour(price=130000, transportation_id=3, hotel_id=2, days=6, Departure_date="2022-09-03", Arrival_date="2022-09-03", name="test"))

print("test")
