import asyncio
import datetime
from typing import Optional
import beanie
import motor.motor_asyncio
import pydantic


async def main():
    await init_connections("beanie_quickstart")
    await create_user()
    await insert_multiple_users()


async def init_connections(db_name: str):
    conn_str = f"mongodb://localhost:27017/{db_name}"
    client = motor.motor_asyncio.AsyncIOMotorClient(conn_str)
    await beanie.init_beanie(client[db_name], document_models=[User])

    print(f"Connected to MongoDB: {db_name}!")


async def create_user():
    count = await User.count()
    if count:
        print(f"{count:,} user(s) already exists!")
        return

    print("Creating new user...")
    loc = Location(city="Taipei", country="TW")
    user = User(name="John", email="john@example.com", location=loc)
    print(f"User before save: {user}")
    await user.save()
    print(f"User after save: {user}")


async def insert_multiple_users():
    count = await User.count()
    if count >= 4:
        print(f"{count:,} user(s) already exists!")
        return

    print("Creating a set of users...")
    user1 = User(name="John", email="john@example.com", location=Location(city="Taipei", country="TW"))
    user2 = User(name="Mary", email="mary@example.com", location=Location(city="TaoYuan", country="TW"))
    user3 = User(name="Bob", email="bob@example.com", location=Location(city="Taichung", country="TW"))

    await User.insert_many([user1, user2, user3])

    print("Inserting users objects.")


class Location(pydantic.BaseModel):
    city: str
    state: Optional[str] = None
    country: str


class User(beanie.Document):
    name: str
    email: str
    password_hash: Optional[str] = None

    created_date: datetime.datetime = pydantic.Field(default_factory=datetime.datetime.now)
    last_login: datetime.datetime = pydantic.Field(default_factory=datetime.datetime.now)

    location: Location


if __name__ == "__main__":
    asyncio.run(main())
