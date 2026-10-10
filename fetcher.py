import requests
from mylogger import MyLogger

logger = MyLogger()


def FetchWeatherData(latitude,longitude,retry=3):
    url = "https://api.open-meteo.com/v1/forecast?"
    params = {
        "latitude":latitude,
        "longitude":longitude,
        "current": "temperature_2m,is_day,wind_speed_10m,wind_direction_10m,rain"
    }
    
    for i in range(0,retry):
        try:
            logger.info("Fetching has just started...")
            response = requests.get(url=url, params=params)
            response.raise_for_status()
            logger.info("Data fetched suscessfully!")
            return response.json()
            
        except requests.RequestException as e:
            logger.error(f"API Failure!!! || URL = {url} || Error = {e}")
