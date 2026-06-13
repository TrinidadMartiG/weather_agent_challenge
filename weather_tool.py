import requests
from dataclasses import dataclass

@dataclass
class Weather:
    city: str
    temperature_c: float
    condition: str

# Step 1 — geocode city name → lat/lon
GEOCODING_URL = "https://geocoding-api.open-meteo.com/v1/search"

# Step 2 — fetch current weather using lat/lon
FORECAST_URL = "https://api.open-meteo.com/v1/forecast"

def get_weather(city: str) -> Weather:
    """Consulta el clima de una ciudad.
    TODO: completar. Considerar tipado, manejo de errores,
    timeout y dejar la función testeable con mocks.
    """
    raise NotImplementedError


if __name__ == "__main__":
    pass
