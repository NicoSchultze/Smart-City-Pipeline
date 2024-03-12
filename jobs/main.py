import os
import uuid

from confluent_kafka import SerializingProducer
import simplejson as json
from datetime import datetime, timedelta
import random

LONDON_COORDINATES = { "latitude": 51.5074, "longitude": -0.1278 }
BIRMINGHAM_COORDINATES = { "latitude": 52.4862, "longitude": -1.8904 }

# Calculate movement increments
LATITUDE_INCREMENT = (BIRMINGHAM_COORDINATES["latitude"] - LONDON_COORDINATES["latitude"]) / 100
LONGITUDE_INCREMENT = (BIRMINGHAM_COORDINATES["longitude"] - LONDON_COORDINATES["longitude"]) / 100

# Environment Variables
KAFKA_BOOTSTRAP_SERVERS = os.getenv('KAFKA_BOOTSTRAP_SERVERS', 'localhost:9092')

VEHICLE_TOPIC = os.getenv('VEHICLE_TOPIC', 'vehicle_data')
GPS_TOPIC = os.getenv('GPS_TOPIC', 'gps_data')
TRAFFIC_TOPIC = os.getenv('TRAFFIC_TOPIC', 'traffic_data')
WEATHER_TOPIC = os.getenv('WEATHER_TOPIC', 'weather_data')
EMERGENCY_TOPIC = os.getenv('EMERGENCY_TOPIC', 'emergency_data')

random.seed(42)
start_time = datetime.now()
start_location = LONDON_COORDINATES.copy()



def get_next_time():
    global start_time
    start_time += timedelta(seconds=random.randint(30, 60)) # update frequency
    return start_time

def generate_gps_data(device_id, timestamp, vehicle_type='private'):
    return {
        'id': uuid.uuid4(),
        'deviceId': device_id,
        'timestamp': timestamp,
        'speed': random.uniform(0,40), #km/h
        'direction': 'North-East',
        'vehicleType': vehicle_type
    }

def generate_weather_data(device_id, timestamp, location):
    return {
        'id': uuid.uuid4(),
        'deviceId': device_id,
        'location': location,
        'timestamp': timestamp,
        'temperature': random.uniform(-5, 25),
        'weatherCondition': random.choice(['Sunny', 'Cloudy', 'Rainy', 'Snow']),
        'precipitation': random.uniform(0, 25),
        'windSpeed': random.uniform(0, 70),
        'humidity': random.randint(0, 100), # percentage
        'airQualityIndex': random.uniform(0, 500) # AQL Value
    }

def generate_emergency_incident_data(device_id, timestamp, location):
    return {
        'id': uuid.uuid4(),
        'deviceId': device_id,
        'IncidentId': uuid.uuid4(),
        'type': random.choice(['Accident', 'Fire', 'Medical', 'Police', 'None']),
        'location': location,
        'timestamp': timestamp,
        'status': random.choice(['Active', 'Resolved']),
        'description': 'Description of the incident'
    }


def generate_traffic_camera_data(device_id, camera_id, timestamp, location):
    return {
        'id': uuid.uuid4(),
        'deviceId': device_id,
        'cameraId': camera_id,
        'location': location,
        'timestamp': timestamp,
        'snapshot': 'Base64EncodedString'
    }

def generate_vehicle_data(device_id):
    location = simulate_vehicle_movement()

    return {
        'id': uuid.uuid4(),
        'deviceId': device_id,
        'timestamp': get_next_time().isoformat(),
        'location': (location['latitude'], location['longitude']),
        'speed': random.uniform(10, 40),
        'direction': 'North-East',
        'make': 'Mercedes',
        'model': 'S-Class',
        'year': 2024,
        'fuelType': 'Hybrid'
    }

def simulate_vehicle_movement():
    global start_location

    # move towards birmingham
    start_location['latitude'] += LATITUDE_INCREMENT
    start_location['longitude'] += LONGITUDE_INCREMENT

    # add some randomness to simulate actual road travel
    start_location['latitude'] += random.uniform(-0.0005, 0.0005)
    start_location['longitude'] += random.uniform(-0.0005, 0.0005)

    return start_location

def simulate_journey(producer, device_id):
    while True:
        vehicle_data = generate_vehicle_data(device_id)
        gps_data = generate_gps_data(device_id, vehicle_data['timestamp'])
        traffic_camera_data = generate_traffic_camera_data(device_id, 'NikonCam1', vehicle_data['timestamp'], vehicle_data['location'])
        weather_data = generate_weather_data(device_id, vehicle_data['timestamp'], vehicle_data['location'])
        emergency_incident_data = generate_emergency_incident_data(device_id,  vehicle_data['timestamp'], vehicle_data['location'])


if __name__ == "__main__":
    # How Kafka is configured
    producer_config = {
        'bootstrap.servers': KAFKA_BOOTSTRAP_SERVERS,
        'error_cb': lambda err: print(f'Kafka error {err}')
    }

    producer = SerializingProducer(producer_config)

    try:
        simulate_journey(producer, 'Vehicle-Nico-1')

    except KeyboardInterrupt:
        print('Simulation ended by the user')

    except Exception as e:
        print(f'Unexpected error occured: {e}')

