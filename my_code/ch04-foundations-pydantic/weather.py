from __future__ import annotations

from typing import Any, Optional

from pydantic import BaseModel


class Weather(BaseModel):
    description: str
    category: str


class Wind(BaseModel):
    speed: float
    deg: float


class Forecast(BaseModel):
    temp: float
    feels_like: float
    pressure: int
    humidity: int
    low: int
    high: int


class Location(BaseModel):
    city: str
    state: Optional[str]
    country: str


class RateLimiting(BaseModel):
    unique_lookups_remaining: int
    lookup_reset_window: str


class WeatherModel(BaseModel):
    weather: Weather
    wind: Wind
    units: str
    forecast: Forecast
    location: Location
    rate_limiting: RateLimiting


data = {
    "weather": {"description": "broken clouds", "category": "Clouds"},
    "wind": {"speed": 2.57, "deg": 80.0},
    "units": "metric",
    "forecast": {
        "temp": 28.52,
        "feels_like": 30.94,
        "pressure": 1008,
        "humidity": 65,
        "low": 27,
        "high": 29,
    },
    "location": {"city": "Taipei", "state": None, "country": "TW"},
    "rate_limiting": {"unique_lookups_remaining": 48, "lookup_reset_window": "1 hour"},
}

report = WeatherModel(**data)

print("The weather is now:")
print(report.weather.description)
