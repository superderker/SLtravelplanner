from datetime import datetime, timedelta
from journey import Journey

from get_station_id import Stations

 
# Function to get the user input for the journeys
def get_journeys(stations: Stations) -> list[Journey]:
    journeys = []
    print("\n"*40)
    journey_amount = int(input("How many journeys do you want to make? "))

    departure_datetime = now = datetime.now()

    # Ask for departure date
    while True:

        departure_date_prompt = input(
            f'Enter the departure date for the journey (in format MM-DD, default is current date): '
        )

        if not departure_date_prompt:
            temp = datetime.now()
        else:
            try:
                temp = datetime.strptime(departure_date_prompt, '%m-%d')
            except ValueError:
                print("Invalid date format. Please try again.")
                continue

        departure_datetime = departure_datetime.replace(
            month=temp.month, day=temp.day)

        if departure_datetime < now:
            print("Departure date cannot be in the past. Please try again.")
            continue

        break

    # Ask for departure time
    while True:
        departure_date_prompt = input(
            f'Enter the departure time for journey the journey (in 24-hour format HH:MM, default is current time): '
        )

        if not departure_date_prompt:
            temp = datetime.now()
        else:
            try:
                temp = datetime.strptime(departure_date_prompt, '%H:%M')
            except ValueError:
                print("Invalid time format. Please try again.")
                continue

        departure_datetime = departure_datetime.replace(
            hour=temp.hour, minute=temp.minute)

        if departure_datetime < now:
            print("Departure time cannot be in the past. Please try again.")
            continue

        break

    # Loop through the number of journeys the user wants to make, and ask information about each journey
    for i in range(1, journey_amount + 1):
        # Ask for departure (origin) station
        while True:
            origin_prompt = input(f'Enter the start station for journey {i}: ')
            result = stations.get_station_and_id(origin_prompt)
            if result is not None:
                origin, origin_id = result
                break

            print("No station found. Please try again.")

        # Ask for the destination station
        while True:
            destination_prompt = input(
                f'Enter the destination station for journey {i}: ')
            result = stations.get_station_and_id(destination_prompt)
            if result is not None:
                destination, destination_id = result
                break

            print("No station found. Please try again.")

        # Ask for transfer time unless it's the last journey
        if i == journey_amount:
            journey_transfer_duration = None
        else:
            while True:
                transfer_duration_prompt = input(
                    f'Enter the transfer time in HH:MM between this journey and journey {i + 1}: ')

                try:
                    temp = datetime.strptime(transfer_duration_prompt, '%H:%M')
                except ValueError:
                    print("Invalid time format. Please try again.")
                    continue

                journey_transfer_duration = timedelta(
                    hours=temp.hour, minutes=temp.minute)
                break

        # Add the journey to the journey_list using the Journey class
        journeys.append(
            Journey(
                origin,
                origin_id,
                destination,
                destination_id,
                departure_datetime,
                None,
                journey_transfer_duration,
                None
            )
        )

    # Return the journey_list for later use
    return journeys
