# Weather API Data Fetcher

A small command-line Python script that asks for a latitude and longitude, fetches the current weather for that location from the [Open-Meteo](https://open-meteo.com/) API, and appends the result to a CSV file.

## What it does

1. Prompts for a latitude and longitude in the terminal.
2. Validates the range (latitude -90 to 90, longitude -180 to 180) and asks again if invalid.
3. Requests current weather data from the Open-Meteo forecast API (no API key required).
4. Retries the request up to 3 times if it fails.
5. Appends one row to `weather_data.csv` (creates the header if the file is empty).
6. Logs each step to the console and to `app.log`.

## Data collected

The following current-weather fields are requested from Open-Meteo, plus the coordinates returned by the API:

| Column | Description |
|---|---|
| `time` | Timestamp of the reading (ISO 8601) |
| `interval` | Data interval in seconds (e.g. `900`) |
| `temperature_2m` | Temperature at 2 m |
| `is_day` | `1` if daytime, `0` if night |
| `wind_speed_10m` | Wind speed at 10 m |
| `wind_direction_10m` | Wind direction at 10 m (degrees) |
| `rain` | Rain amount |
| `latitude` | Latitude returned by the API |
| `longitude` | Longitude returned by the API |

Units are Open-Meteo's defaults (°C, km/h, mm). The API may snap your input coordinates to its nearest grid point, so the saved latitude/longitude can differ slightly from what you typed.

## Project structure

```
weather-api-fetcher/
├── main.py          # Entry point: user input, validation, orchestration
├── fetcher.py       # Calls the Open-Meteo API (with retry)
├── csv_writer.py    # Appends a record to weather_data.csv
├── mylogger.py      # Logger setup (console + rotating file)
├── weather_data.csv # Output data (appended on every run)
└── app.log          # Log output (rotates at 10 MB, 4 backups)
```

## Requirements

- Python 3
- [`requests`](https://pypi.org/project/requests/)

There is no `requirements.txt` yet, so install the dependency manually:

```bash
pip install requests
```

## Usage

```bash
python main.py
```

Example session:

```
Enter the value of latitude: 26.45
Enter the value of longitude: 87.27
```

The fetched record is printed/logged and a new row is added to `weather_data.csv`.

## Current limitations

- **Single location per run:** the script handles one coordinate pair, then exits.
- **No error handling for bad input type:** entering non-numeric text for latitude or longitude raises a `ValueError` and stops the script.
- **Failed fetches are not handled in `main.py`:** if all 3 retry attempts fail, `FetchWeatherData` returns `None` and the script crashes with a `TypeError` afterwards. The failure itself is logged in `app.log`.
- **Retries have no delay or request timeout.**
- **No duplicate check:** running the same coordinates repeatedly adds repeated rows (the API's `time` value only updates every 15 minutes).
- **No tests and no `requirements.txt`.**
- Coordinates are entered as latitude first, then longitude. Swapping them still passes validation when the values are in range, so double-check the order.

## Possible next steps

- Handle non-numeric input and failed fetches gracefully
- Add a request timeout and a delay between retries
- Add a `requirements.txt`
- Accept coordinates via command-line arguments or a city name

## Data source

Weather data is provided by [Open-Meteo](https://open-meteo.com/).