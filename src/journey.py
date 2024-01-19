from dataclasses import dataclass
from datetime import datetime, timedelta
from typing import Optional

 
@dataclass
class Journey:
    origin: str
    origin_id: str
    destination: str
    destination_id: str
    departure_datetime: datetime
    arrival_time: Optional[datetime]
    journey_transfer_duration: Optional[timedelta]
    transportation_mode: Optional[str]
