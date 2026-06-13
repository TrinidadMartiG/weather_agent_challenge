# Weather Agent Challenge

## Tarea

Tienes una tool incompleta que consulta el clima de una ciudad llamando a una API externa.

Completa la función `get_weather(city: str)` en `weather_tool.py` para que:

1. Resuelva el nombre de la ciudad a latitud y longitud
2. Consulte el clima actual y devuelva un objeto `Weather` tipado
3. Maneje errores: fallo de red y ciudad no encontrada
4. Use un timeout apropiado
5. Sea testeable con mocks (sin hacer llamadas reales a la API)

Luego completa los dos tests en `test_weather_tool.py`.

**Puedes usar Claude Code, Copilot u otro asistente de IA.** No se evalúa si puedes hacerlo sin él — evaluaremos cómo piensas y trabajas con él.

---

## API de referencia — Open-Meteo

No requiere API key. Gratuita para uso no comercial.

Documentación oficial: https://open-meteo.com/en/docs

---

### Paso 1 — Geocodificación (ciudad → lat/lon)

**Endpoint:** `GET https://geocoding-api.open-meteo.com/v1/search`

Documentación: https://open-meteo.com/en/docs/geocoding-api

| Parámetro  | Tipo   | Descripción                        |
|------------|--------|------------------------------------|
| `name`     | string | Nombre de la ciudad                |
| `count`    | int    | Cuántos resultados devolver (usar `1`) |
| `language` | string | Idioma de los resultados (`en`)    |
| `format`   | string | Formato de respuesta (`json`)      |

**Ejemplo de request:**
```
GET https://geocoding-api.open-meteo.com/v1/search?name=Santiago&count=1&language=en&format=json
```

**Ejemplo de respuesta (ciudad encontrada):**
```json
{
  "results": [
    {
      "name": "Santiago",
      "latitude": -33.45694,
      "longitude": -70.64827,
      "country": "Chile"
    }
  ]
}
```

**Respuesta cuando la ciudad no existe:** el campo `results` está ausente o es una lista vacía.

---

### Paso 2 — Clima actual (lat/lon → temperatura y condición)

**Endpoint:** `GET https://api.open-meteo.com/v1/forecast`

| Parámetro   | Tipo   | Descripción                                               |
|-------------|--------|-----------------------------------------------------------|
| `latitude`  | float  | Latitud obtenida en el paso 1                             |
| `longitude` | float  | Longitud obtenida en el paso 1                            |
| `current`   | string | Variables a incluir: `temperature_2m,weathercode`         |

**Ejemplo de request:**
```
GET https://api.open-meteo.com/v1/forecast?latitude=-33.46&longitude=-70.65&current=temperature_2m,weathercode
```

**Ejemplo de respuesta:**
```json
{
  "current": {
    "temperature_2m": 18.4,
    "weathercode": 3
  }
}
```

---

### Códigos de clima WMO (`weathercode`)

Usa esta tabla para convertir el código numérico al campo `condition: str` del objeto `Weather`.

| Código     | Condición               |
|------------|-------------------------|
| 0          | Clear sky               |
| 1, 2, 3    | Partly cloudy           |
| 45, 48     | Fog                     |
| 51, 53, 55 | Drizzle                 |
| 61, 63, 65 | Rain                    |
| 71, 73, 75 | Snow                    |
| 80, 81, 82 | Rain showers            |
| 95         | Thunderstorm            |
| 96, 99     | Thunderstorm with hail  |

Referencia completa: https://open-meteo.com/en/docs#weathervariables

---

## Setup

Crea y activa un entorno virtual antes de instalar las dependencias:

```bash
# Crear el entorno virtual
python -m venv .venv

# Activarlo
# macOS / Linux
source .venv/bin/activate

# Windows
.venv\Scripts\activate
```

Una vez activo, instala las dependencias:

```bash
pip install -e ".[dev]"
```

> Verifica que el entorno esté activo: el prompt del terminal debe mostrar `(.venv)` al inicio.

## Correr los tests

```bash
python -m pytest test_weather_tool.py -v
```

Los tests deben pasar sin hacer llamadas reales a la API.
