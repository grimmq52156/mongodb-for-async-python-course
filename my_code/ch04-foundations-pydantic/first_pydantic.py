import datetime
from typing import Optional

import pydantic


class Item(pydantic.BaseModel):
    item_id: int
    created_date: datetime.datetime
    page_visited: list[int]
    price: float
    name: Optional[str] = None


def main():
    data = {
        "item_id": "123",
        "created_date": "2018-09-30 12:20",
        "page_visited": [1, 2, "3"],
        "price": 17.22,
    }

    item = Item(**data)

    print(item)


if __name__ == "__main__":
    main()
