from datetime import datetime
import requests
from typing import Optional

from journey import Journey
from get_station_id import Stations
from user_input import get_journeys
 

# Class to make the API call to ResRobot v.2.1 API and return the results
class ResRobot:
    def __init__(self, api_key: str):

        self.api_key = api_key

    def API_call(self, journey: Journey, num_f: int = 6, num_b: int = 0, max_change: int = 0) -> Optional[list[Journey]]:

        # Store the results from the API call
        trips = []

        params = {
            'accessId': self.api_key,
            'originId': journey.origin_id,
            'destId': journey.destination_id,
            'date': datetime.strftime(journey.departure_datetime, '%Y-%m-%d'),
            'time': datetime.strftime(journey.departure_datetime, '%H:%M'),
            'format': 'json',
            'numF': num_f,
            'numB': num_b,
            'lang': 'en',
            'maxChange': max_change,
            'originWalk': 0
        }

        url = 'https://api.resrobot.se/v2.1/trip'

        response = requests.get(url, params=params)

        data = response.json()

        if response.status_code != 200:
            print(f'Error when making API call: {data}')
            return

        for trip in data['Trip']:

            # Get the departure and arrival time for the journey
            trip_data = trip['LegList']['Leg'][0]

            journey_departure_time = trip_data['Origin']['time']
            journey_departure_date = trip_data['Origin']['date']
            journey_departure_date_time = datetime.strptime(
                f'{journey_departure_date} {journey_departure_time}', '%Y-%m-%d %H:%M:%S')

            journey_arrival_time = trip_data['Destination']['time']
            journey_arrival_date = trip_data['Destination']['date']
            journey_arrival_date_time = datetime.strptime(
                f'{journey_arrival_date} {journey_arrival_time}', '%Y-%m-%d %H:%M:%S')

            trips.append(Journey(journey.origin,
                                 journey.origin_id,
                                 journey.destination,
                                 journey.destination_id,
                                 journey_departure_date_time,
                                 journey_arrival_date_time,
                                 journey.journey_transfer_duration,
                                 trip_data['name']))

        return trips

    # Match the remaining journeys to the first journey
    def manage_journeys(self, stations: Stations) -> list[list[Journey]]:

        journeys_input = get_journeys(stations)

        # Array of arrays that stores each possible journey, each subarray is a journey at a different point in time
        journey_information = [[trip]
                               for trip in self.API_call(journeys_input[0])]

        # Loop through the remaining journeys and match them to the first journey
        for i in range(1, len(journeys_input)):
            for journey in journey_information:
                journeys_input[i].departure_datetime = journey[-1].arrival_time + \
                    journeys_input[i-1].journey_transfer_duration

                matched_journey = self.API_call(journeys_input[i], num_f=1)

                journey.append(matched_journey[0])

        return journey_information
