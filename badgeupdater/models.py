from dataclasses import dataclass


@dataclass
class BadgeUpdateRequest:
    id: str


@dataclass
class BadgeUpdateResponse:
    players: list[str]
