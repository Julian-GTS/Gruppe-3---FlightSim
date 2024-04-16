    
import random
import string

from . import flight_data
import json


def write_flight_data_to_file(flight_data, file_path):
    with open(file_path, "w") as file:
        file.write(json.dumps(flight_data.to_json(), indent=4))

def generate_flight_data():
    aircraft = random.choice(["Boeing 747", "Airbus A320", "Cessna 172"])
    flight_number = ''.join(random.choices(string.ascii_uppercase + string.digits, k=6))
    origin = random.choice(["JFK", "LAX", "ORD", "ATL"])
    destination = random.choice(["LHR", "CDG", "FRA", "AMS"])
    departure_time = "2022-01-01T" + str(random.randint(0, 23)).zfill(2) + ":" + str(random.randint(0, 59)).zfill(2) + ":00Z"
    arrival_time = "2022-01-01T" + str(random.randint(0, 23)).zfill(2) + ":" + str(random.randint(0, 59)).zfill(2) + ":00Z"
    latitude = round(random.uniform(-90, 90), 4)
    longitude = round(random.uniform(-180, 180), 4)
    altitude = random.randint(10000, 50000)
    position = {
        "latitude": latitude,
        "longitude": longitude,
        "altitude": altitude
    }
    indicated_air_speed = random.randint(200, 400)
    true_air_speed = random.randint(400, 600)
    ground_speed = random.randint(400, 600)
    speed = {
        "indicatedAirSpeed": indicated_air_speed,
        "trueAirSpeed": true_air_speed,
        "groundSpeed": ground_speed
    }
    pitch = random.uniform(-10, 10)
    roll = random.uniform(-10, 10)
    yaw = random.uniform(-10, 10)
    orientation = {
        "pitch": pitch,
        "roll": roll,
        "yaw": yaw
    }
    takeoff_smoothness = round(random.uniform(0, 10), 1)
    landing_smoothness = round(random.uniform(0, 10), 1)
    navigation_accuracy = round(random.uniform(0, 10), 1)
    communication_clarity = round(random.uniform(0, 10), 1)
    pilot_rating = {
        "takeoffSmoothness": takeoff_smoothness,
        "landingSmoothness": landing_smoothness,
        "navigationAccuracy": navigation_accuracy,
        "communicationClarity": communication_clarity
    }
    
    return flight_data.FlightData(
        aircraft=aircraft,
        flight_number=flight_number,
        origin=origin,
        destination=destination,
        departure_time=departure_time,
        arrival_time=arrival_time,
        position=position,
        speed=speed,
        orientation=orientation,
        pilot_rating=pilot_rating
    )