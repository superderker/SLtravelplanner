from journey import Journey

# Print the results 


def print_journey_information(journey_information: list[list[Journey]]):

    # Print the final results
    for journey in journey_information:
        for i, trip in enumerate(journey):

            print(f'\nJourney {i+1}:')
            print(f'Take {trip.transportation_mode.strip().replace("Länstrafik - ", "").replace("Länstrafik -", "")}',
                  f'from {trip.origin.strip().capitalize()}',
                  f'to {trip.destination.strip().capitalize()}')

            print(f'Departure time: {trip.departure_datetime}')
            print(f'Arrival time: {trip.arrival_time}')

            if trip.journey_transfer_duration is not None:

                seconds = (journey[i+1].departure_datetime -
                           trip.arrival_time).total_seconds()
                hours, seconds = map(int, divmod(seconds, 3600))
                minutes, seconds = divmod(seconds, 60)

                print(
                    f'\nWalk to journey {i+2}, you have {f"{hours} hours and "if hours != 0 else ""}{int(minutes)} minutes until departure!')

        print(
            f'Total travel time: {journey[-1].arrival_time - journey[0].departure_datetime}')
        print("-"*32)
