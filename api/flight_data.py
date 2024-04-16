import random
import string

class FlightData:
    def __init__(self, aircraft, flight_number, origin, destination, departure_time, arrival_time, position, speed, orientation, pilot_rating):
        self.aircraft = aircraft
        self.flight_number = flight_number
        self.origin = origin
        self.destination = destination
        self.departure_time = departure_time
        self.arrival_time = arrival_time
        self.position = position
        self.speed = speed
        self.orientation = orientation
        self.pilot_rating = pilot_rating

    def to_json(self):
        return {
            "aircraft": self.aircraft,
            "flightNumber": self.flight_number,
            "origin": self.origin,
            "destination": self.destination,
            "departureTime": self.departure_time,
            "arrivalTime": self.arrival_time,
            "position": self.position,
            "speed": self.speed,
            "orientation": self.orientation,
            "pilotRating": self.pilot_rating
        }