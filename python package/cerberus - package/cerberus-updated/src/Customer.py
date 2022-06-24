from dataclasses import dataclass


@dataclass
class Customer:
    id: int
    name: str
    accounts: list
    contact_details: dict
