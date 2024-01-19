import csv
from typing import Optional

from thefuzz import fuzz, process


# This class is used to match the user input with the correct station id. 
class Stations:
    def __init__(self, file_name):
        # Read the csv file and create a dictionary with the station name as key and station id as value.
        with open(file_name, 'r', encoding="utf-8-sig") as f:
            self.stations: dict[str, str] = {
                row["stop_name"].lower().replace("stockholm", '').replace("station", '').replace("t-bana", '').strip(): row["stop_id"] for row
                in csv.DictReader(f)}

    # Function to get the station id from the station name
    def get_station_and_id(self, station_name: str, match_similarity_threshold: int = 70) -> Optional[tuple[str, str]]:
        # Remove the words "Stockholm" and "Station" from the station name and convert to lowercase
        station_name = station_name.lower().replace(
            "stockholm", "").replace("station", "").replace("t-bana", "").strip()

        # Use thefuzz to find the closest match to the station name in the dictionary
        closest_match = process.extractOne(
            query=station_name,
            choices=self.stations.keys(),
            scorer=fuzz.token_sort_ratio,
            score_cutoff=match_similarity_threshold
        )

        # Return None if no match is found
        if closest_match is None:
            return

        # Return the station and station id if the match is above the match_similarity_threshold, otherwise return None
        return closest_match[0], self.stations[closest_match[0]]
