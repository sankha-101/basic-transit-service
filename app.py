from flask import Flask, request, jsonify
from datetime import datetime, timedelta

app = Flask(__name__)

transit_schedules = [
    {
        "transit_mode": "rail",
        "eta_origin": (datetime.now() + timedelta(minutes=10)).strftime('%Y-%m-%d %H:%M:%S'),
        "eta_destination": (datetime.now() + timedelta(minutes=50)).strftime('%Y-%m-%d %H:%M:%S')
    },
    {
        "transit_mode": "bus",
        "eta_origin": (datetime.now() + timedelta(minutes=15)).strftime('%Y-%m-%d %H:%M:%S'),
        "eta_destination": (datetime.now() + timedelta(minutes=45)).strftime('%Y-%m-%d %H:%M:%S')
    },
    {
        "transit_mode": "light_rail",
        "eta_origin": (datetime.now() + timedelta(minutes=20)).strftime('%Y-%m-%d %H:%M:%S'),
        "eta_destination": (datetime.now() + timedelta(minutes=40)).strftime('%Y-%m-%d %H:%M:%S')
    },
]

@app.route('/transit_schedule', methods=['POST'])
def get_transit_schedule():
    data = request.get_json()

    origin_station_id = data.get('origin_station_id')
    coordinates = data.get('coordinates')
    destination_station_id = data.get('destination_station_id')

    if not origin_station_id or not coordinates or not destination_station_id:
        return jsonify({'error': 'Invalid input'}), 400

    latitude = coordinates.get('latitude')
    longitude = coordinates.get('longitude')

    if not latitude or not longitude:
        return jsonify({'error': 'Invalid coordinates'}), 400
    response = {
        "next_schedules": transit_schedules
    }

    return jsonify(response), 200

if __name__ == '__main__':
    app.run(debug=True)
