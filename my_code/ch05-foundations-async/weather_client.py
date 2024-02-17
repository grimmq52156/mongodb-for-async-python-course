import asyncio

import httpx

locations = [
    "https://ribo-fastapi.internal/api/weather/taipei&country=TW",
    "https://ribo-fastapi.internal/api/weather/taichung&country=TW",
    "https://ribo-fastapi.internal/api/weather/kaohsiung&country=TW",
    "https://ribo-fastapi.internal/api/weather/taoyuan&country=TW",
    "https://ribo-fastapi.internal/api/weather/tainan&country=TW",
    "https://ribo-fastapi.internal/api/weather/hsinchu&country=TW",
    "https://ribo-fastapi.internal/api/weather/keelung&country=TW",
    "https://ribo-fastapi.internal/api/weather/chiayi&country=TW",
    "https://ribo-fastapi.internal/api/weather/pingtung&country=TW",
    "https://ribo-fastapi.internal/api/weather/yilan&country=TW",
]


async def get_report(url: str):
    print(f"Calling {url}")
    async with httpx.AsyncClient(verify=False) as client:
        resp = await client.get(url)
        resp.raise_for_status()

    return resp.json()


async def main():
    tasks = [asyncio.create_task(get_report(url)) for url in locations]
    for task in tasks:
        report = await task
        show_report(report)

    print("Done!")


def show_report(report):
    print(report)


if __name__ == "__main__":
    asyncio.run(get_report(locations[0]))
