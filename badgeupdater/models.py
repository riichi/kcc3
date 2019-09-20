from dataclasses import dataclass
from typing import List


@dataclass
class BadgeUpdateRequest:
    id: str


@dataclass
class BadgeUpdateResponse:
    players: List[str]
