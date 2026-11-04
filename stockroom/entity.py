from dataclasses import dataclass


@dataclass
class Order:
    id: int
    title: str
    status: str = "open"
