import datetime
from typing import Optional

import beanie
import pydantic


def main():
    print("Creating new user...")
    loc = Location(city="Taipei", country="TW")
    user = User(name="John", email="john@example.com", location=loc)

    print("User created!")


class Location(pydantic.BaseModel):
    city: str
    state: Optional[str]
    country: str


class User(beanie.Document):
    name: str
    email: str
    password_hash: Optional[str]

    created_date: datetime.datetime = pydantic.Field(default_factory=datetime.datetime.now)
    last_login: datetime.datetime = pydantic.Field(default_factory=datetime.datetime.now)

    location: Location


if __name__ == "__main__":
    main()
