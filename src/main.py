import os
from pathlib import Path 

from dotenv import load_dotenv

from get_station_id import Stations
from print_results import print_journey_information
from res_robot import ResRobot

PROJECT_ROOT = Path(__file__).parent.parent


def main():
    load_dotenv()

    stations = Stations(f'{PROJECT_ROOT}/resources/stops.csv')
    resrobot = ResRobot(os.getenv("API_KEY"))
    result = resrobot.manage_journeys(stations)
    print_journey_information(result)


if __name__ == "__main__":
    main()
